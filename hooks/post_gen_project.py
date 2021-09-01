import os
import shutil


def generate_license():
    if "{{cookiecutter.license}}" != "None":
        os.rename(os.path.join("LICENSES", "{{cookiecutter.license}}"), "LICENSE")
    shutil.rmtree("LICENSES")


def remove_dotgitlabciyml_file():
    os.remove(".gitlab-ci.yml")


def remove_github_actions():
    shutil.rmtree(".github")


def remove_bitbucket_pipeline_yml_file():
    os.remove("bitbucket-pipelines.yml")

if __name__ == "__main__":
    generate_license()
    if "{{cookiecutter.ci_tool}}" != "GitLab":
        remove_dotgitlabciyml_file()
    if "{{cookiecutter.ci_tool}}" != "GitHub":
        remove_github_actions()
    if "{{cookiecutter.ci_tool}}" != "Bitbucket":
        remove_bitbucket_pipeline_yml_file()
