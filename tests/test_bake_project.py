import os
import re
import pytest
import subprocess
import shutil
import yaml
from cookiecutter.exceptions import FailedHookException
from binaryornot.check import is_binary

PATTERN = r"{{(\s?cookiecutter)[.](.*?)}}"
RE_OBJ = re.compile(PATTERN)


def _fixture_id(ctx):
    """Helper to get a user-friendly test name from the parametrized context."""
    return "-".join(f"{key}:{value}" for key, value in ctx.items())


def build_files_list(root_dir):
    """Build a list containing absolute paths to the generated files."""
    return [
        os.path.join(dirpath, file_path)
        for dirpath, subdirs, files in os.walk(root_dir)
        for file_path in files
    ]


def check_paths(paths):
    """Method to check all paths have correct substitutions."""
    # Assert that no match is found in any of the files
    for path in paths:
        if is_binary(path):
            continue

        for line in open(path, "r"):
            match = RE_OBJ.search(line)
            assert match is None, f"cookiecutter variable not replaced in {path}"


@pytest.mark.parametrize("context_override", pytest.SUPPORTED_COMBINATIONS, ids=_fixture_id)
def test_bake_project(cookies, context, context_override):
    """Test that project is generated and fully rendered."""
    result = cookies.bake(extra_context={**context, **context_override})
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == context["project_slug"]
    assert result.project_path.is_dir()

    paths = build_files_list(str(result.project_path))
    assert paths
    check_paths(paths)


@pytest.mark.parametrize("stage, expected_test_script",
                         [("linting:flake8", ["make ${LINTING_PKG}"]),
                          ("linting:mypy", ["make ${LINTING_PKG}"]),
                          ("linting:bandit", ["make ${LINTING_PKG}"]),
                          ("test:3.8", ["make test"]),
                          ("test:3.9", ["make test"]),
                          ("test:3.10", ["make test"]),
                          ("test:3.11", ["make test"])
                          ])
def test_gitlab_invokes_linting_and_pytest(cookies, context, stage,
                                           expected_test_script):
    context.update({"ci_tool": "GitLab"})
    result = cookies.bake(extra_context=context)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == context["project_slug"]
    assert result.project_path.is_dir()

    with open(f"{result.project_path}/.gitlab-ci.yml", "r") as gitlab_yml:
        try:
            gitlab_config = yaml.safe_load(gitlab_yml)
            assert gitlab_config[stage]["script"] == expected_test_script
        except yaml.YAMLError as e:
            pytest.fail(e)


@pytest.mark.parametrize("slug", ["project slug", "Project_Slug"])
def test_invalid_slug(cookies, context, slug):
    """Invalid slug should fail pre-generation hook."""
    context.update({"project_slug": slug})

    result = cookies.bake(extra_context=context)

    assert result.exit_code != 0
    assert isinstance(result.exception, FailedHookException)


@pytest.mark.parametrize("invalid_context", pytest.UNSUPPORTED_COMBINATIONS)
def test_error_if_incompatible(cookies, context, invalid_context):
    """It should not generate project an incompatible combination is selected.
    """
    context.update(invalid_context)
    result = cookies.bake(extra_context=context)

    assert result.exit_code != 0
    assert isinstance(result.exception, FailedHookException)


def general_check(cookies, context_override, check_command, extra_requirements=None):
    """Decorator function for setting up test environment"""
    result = cookies.bake(extra_context=context_override)
    project_path = str(result.project_path)
    current_dir = os.getcwd()
    if extra_requirements is None:
        extra_requirements = []
    try:
        os.chdir(project_path)
        if extra_requirements:
            extra_requirements = "&& pip install {} ".format(" ".join(extra_requirements))
        else:
            extra_requirements = ""
        subprocess.run("python3 -m venv venv_tmp "
                       "&& source ./venv_tmp/bin/activate "
                       "&& pip install -r ./requirements/dev.txt "
                       "&& pip install -r ./requirements/docs.txt "
                       "{extra_requirements} "
                       "&& {check_command}".format(check_command=check_command,
                                                   extra_requirements=extra_requirements),
                       shell=True)
    except Exception as e:
        pytest.fail(str(e))
    finally:
        os.chdir(current_dir)
        shutil.rmtree(project_path)


@pytest.mark.parametrize("context_override", pytest.SUPPORTED_COMBINATIONS, ids=_fixture_id)
def test_linting_pytest_twine_passes(cookies, context_override):
    """Generated project should pass flake8."""
    general_check(cookies, context_override,
                  "make flake8 && make mypy && make bandit && make test "
                  "&& make build_whl && twine check {} && cd docs && make html".format(os.path.join("dist", "*.whl")),
                  extra_requirements=["twine"])
