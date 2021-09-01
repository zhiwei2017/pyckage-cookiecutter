from __future__ import print_function


def validate_project_slug():
    project_slug = "{{ cookiecutter.project_slug }}"
    if hasattr(project_slug, "isidentifier"):
        assert (project_slug.isidentifier()), "'{}' project slug is not a valid Python identifier.".format(project_slug)

    assert (project_slug == project_slug.lower()), "'{}' project slug should be all lowercase".format(project_slug)


def validate_author():
    assert ("\\" not in "{{ cookiecutter.author }}"), "Don't include backslashes in author."


if __name__ == "__main__":
    validate_project_slug()
    validate_author()
