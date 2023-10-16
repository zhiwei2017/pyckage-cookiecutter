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

def display_message_to_user():
    cicd_message = "setup the CI/CD pipeline and " if "{{cookiecutter.ci_tool}}" != "None" else ""
    message = f"\033[1mPlease read the comments from README.rst in your project to get to know how to {cicd_message}use commands from Makefile.\033[0m"
    print(message)

if __name__ == "__main__":
    generate_license()
    if "{{cookiecutter.ci_tool}}" != "GitLab":
        remove_dotgitlabciyml_file()
    if "{{cookiecutter.ci_tool}}" != "GitHub":
        remove_github_actions()
    if "{{cookiecutter.ci_tool}}" != "Bitbucket":
        remove_bitbucket_pipeline_yml_file()
    display_message_to_user()
