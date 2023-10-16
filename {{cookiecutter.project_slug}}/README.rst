{{cookiecutter.project_name}}
{% for _ in cookiecutter.project_name %}={% endfor %}

..
    {% if cookiecutter.ci_tool == "GitHub" %}GitHub Actions
    ~~~~~~~~~~~~~~

    You can find all the configuration files of GitHub Actions in ``.github/workflows`` folder.

    Content
    :::::::

    +-------------+----------------------------------------------+--------------------------------------------------+-----------------------------+-----------------------------------------------------------+
    | Config File |          Steps                               |                Trigger Rules                     | Requisite CI/CD Variables   | CI/CD Variables description                               |
    +=============+==============================================+==================================================+=============================+===========================================================+
    |             | mypy check                                   |                                                  |                             |                                                           |
    |             +----------------------------------------------+                                                  |                             |                                                           |
    |             | flake8 check                                 | + **Pushes** to *master/develop* branches        |                             |                                                           |
    |             +----------------------------------------------+                                                  |                             |                                                           |
    | test.yml    | bandit check                                 | + **Pull Requests** to *master/develop* branches |                             |                                                           |
    |             +----------------------------------------------+                                                  |                             |                                                           |
    |             | test with python 3.8 (Ubuntu/Mac OS/Windows) |                                                  |                             |                                                           |
    |             +----------------------------------------------+                                                  |                             |                                                           |
    |             | test with python 3.9 (Ubuntu/Mac OS/Windows) |                                                  |                             |                                                           |
    |             +----------------------------------------------+                                                  |                             |                                                           |
    |             | test with python 3.10 (Ubuntu/Mac OS/Windows)|                                                  |                             |                                                           |
    |             +----------------------------------------------+                                                  |                             |                                                           |
    |             | test with python 3.11 (Ubuntu/Mac OS/Windows)|                                                  |                             |                                                           |
    |             +----------------------------------------------+                                                  |                             |                                                           |
    |             | twine check the built package                |                                                  |                             |                                                           |
    +-------------+----------------------------------------------+--------------------------------------------------+-----------------------------+-----------------------------------------------------------+
    |             |                                              |                                                  |                             | Token for uploading package to official PyPi. If you're   |
    |             |                                              |                                                  | POETRY_PYPI_TOKEN_PYPI      | using a private artifactory, please use the variables     |
    |             |                                              |                                                  |                             | `PACKAGE_INDEX_REPOSITORY_URL`, `PACKAGE_INDEX_USERNAME`, |
    |             |                                              |                                                  |                             | and `PACKAGE_INDEX_PASSWORD` instead.                     |
    |             |                                              |                                                  +-----------------------------+-----------------------------------------------------------+
    |             |                                              |                                                  | PACKAGE_INDEX_REPOSITORY_URL| URL of Private package index.                             |
    | release.yml | deploy to PyPi                               | **Pushes** to tags matching *vXX.XX.XX*          +-----------------------------+-----------------------------------------------------------+
    |             |                                              |                                                  | PACKAGE_INDEX_USERNAME      | Username of Private package index.                        |
    |             |                                              |                                                  +-----------------------------+-----------------------------------------------------------+
    |             |                                              |                                                  | PACKAGE_INDEX_PASSWORD      | Password of Private package index.                        |
    +-------------+----------------------------------------------+--------------------------------------------------+-----------------------------+-----------------------------------------------------------+
    | sphinx.yml  | deploy GitHub pages                          | **Pushes** to *master* branch                    |                             |                                                           |
    +-------------+----------------------------------------------+--------------------------------------------------+-----------------------------+-----------------------------------------------------------+

    **Note**:

    + Before publishing the GitHub pages of your project for the first time, please manually create the branch **gh-pages** via::

        $ git checkout master
        $ git checkout -b gh-pages
        $ git push origin gh-pages

    Setup Steps
    :::::::::::

    1. Go to **Settings**.
    2. Click **Secrets** section.
    3. Click **New repository secret** button.
    4. Input the name and value of a CI/CD variable.

    {% elif cookiecutter.ci_tool == "GitLab" %}GitLab CI
    ~~~~~~~~~

    The file ``.gitlab-ci.yml`` contains all the configurations for GitLab CI.

    Content
    :::::::

    +---------+---------------------------------+-------------------------------------------+------------------------------+-----------------------------------------------------------+
    | Stages  |          Steps                  |                Trigger Rules              | Requisite CI/CD Variables    | CI/CD Variables description                               |
    +=========+=================================+===========================================+==============================+===========================================================+
    |         | mypy check                      |                                           |                              |                                                           |
    |         +---------------------------------+                                           |                              |                                                           |
    | linting | flake8 check                    | + **Pushes** to *master/develop* branches |                              |                                                           |
    |         +---------------------------------+                                           |                              |                                                           |
    |         | bandit check                    | + Any **Merge Requests**                  |                              |                                                           |
    +---------+---------------------------------+                                           |                              |                                                           |
    |         | test with python 3.8            |                                           |                              |                                                           |
    |         +---------------------------------+                                           |                              |                                                           |
    |  test   | test with python 3.9            |                                           |                              |                                                           |
    |         +---------------------------------+                                           |                              |                                                           |
    |         | test with python 3.10           |                                           |                              |                                                           |
    |         +---------------------------------+                                           |                              |                                                           |
    |         | test with python 3.11           |                                           |                              |                                                           |
    +---------+---------------------------------+                                           |                              |                                                           |
    | build   | twine check the built package   |                                           |                              |                                                           |
    +---------+---------------------------------+-------------------------------------------+------------------------------+-----------------------------------------------------------+
    |         |                                 |                                           |                              | Token for uploading package to official PyPi. If you're   |
    |         |                                 |                                           | POETRY_PYPI_TOKEN_PYPI       | using a private artifactory, please use the variables     |
    |         |                                 |                                           |                              | `PACKAGE_INDEX_REPOSITORY_URL`, `PACKAGE_INDEX_USERNAME`, |
    |         |                                 |                                           |                              | and `PACKAGE_INDEX_PASSWORD` instead.                     |
    |         |                                 |                                           +------------------------------+-----------------------------------------------------------+
    | deploy  | deploy to PyPi                  | **Pushes** to tags matching *vXX.XX.XX*   | PACKAGE_INDEX_REPOSITORY_URL | URL of Private package index.                             |
    |         |                                 |                                           +------------------------------+-----------------------------------------------------------+
    |         |                                 |                                           | PACKAGE_INDEX_USERNAME       | Username of Private package index.                        |
    |         |                                 |                                           +------------------------------+-----------------------------------------------------------+
    |         |                                 |                                           | PACKAGE_INDEX_PASSWORD       | Password of Private package index.                        |
    +---------+---------------------------------+-------------------------------------------+------------------------------+-----------------------------------------------------------+

    Setup Steps
    :::::::::::

    1. Go to **Settings**.
    2. Click **CI/CD** section.
    3. Go to **Variables** section.
    4. Click **Add variable** button.
    5. Input the name and value of a CI/CD variable.

        By default, the flag **protected** is checked, which means the added variable can only be used for protected branches/tags.
        If you want to keep your variable protected, please add wildcards **v*** as protected tags in **Settings** -> **Repository** -> **Protected tags**.

        Or you can uncheck the box to use the variable for all branches and tags.

    {% elif cookiecutter.ci_tool == "Bitbucket" %}Bitbucket Pipelines
    ~~~~~~~~~~~~~~~~~~~

    The file ``bitbucket-pipelines.yml`` contains all the configurations of Bitbucket Pipelines.

    Content
    :::::::

    +---------------------------------+-------------------------------------------+------------------------------+-----------------------------------------------------------+
    |          Steps                  |                Trigger Rules              | Requisite CI/CD Variables    | CI/CD Variables description                               |
    +=================================+===========================================+==============================+===========================================================+
    | mypy check                      |                                           |                              |                                                           |
    +---------------------------------+                                           |                              |                                                           |
    | flake8 check                    | + **Pushes** to *master/develop* branches |                              |                                                           |
    +---------------------------------+                                           |                              |                                                           |
    | bandit check                    | + Any **Pull Requests**                   |                              |                                                           |
    +---------------------------------+                                           |                              |                                                           |
    | test with python 3.8            |                                           |                              |                                                           |
    +---------------------------------+                                           |                              |                                                           |
    | test with python 3.9            |                                           |                              |                                                           |
    +---------------------------------+                                           |                              |                                                           |
    | test with python 3.10           |                                           |                              |                                                           |
    +---------------------------------+                                           |                              |                                                           |
    | test with python 3.11           |                                           |                              |                                                           |
    +---------------------------------+                                           |                              |                                                           |
    | twine check the built package   |                                           |                              |                                                           |
    +---------------------------------+-------------------------------------------+------------------------------+-----------------------------------------------------------+
    |                                 |                                           |                              | Token for uploading package to official PyPi. If you're   |
    |                                 |                                           | POETRY_PYPI_TOKEN_PYPI       | using a private artifactory, please use the variables     |
    |                                 |                                           |                              | `PACKAGE_INDEX_REPOSITORY_URL`, `PACKAGE_INDEX_USERNAME`, |
    |                                 |                                           |                              | and `PACKAGE_INDEX_PASSWORD` instead.                     |
    | deploy to PyPi                  | **Pushes** to tags matching *vXX.XX.XX*   +------------------------------+-----------------------------------------------------------+
    |                                 |                                           | PACKAGE_INDEX_REPOSITORY_URL | URL of Private package index.                             |
    |                                 |                                           +------------------------------+-----------------------------------------------------------+
    |                                 |                                           | PACKAGE_INDEX_USERNAME       | Username of Private package index.                        |
    |                                 |                                           +------------------------------+-----------------------------------------------------------+
    |                                 |                                           | PACKAGE_INDEX_PASSWORD       | Password of Private package index.                        |
    +---------------------------------+-------------------------------------------+------------------------------+-----------------------------------------------------------+

    Setup Steps
    :::::::::::

    1. Go to **Repository settings**.
    2. Click **Repository variables**.
    3. Click **add** button.
    4. Input the name and value of a CI/CD variable.

        You need to enable pipelines before adding a new variable for the first time.
    {% endif %}
    Makefile
    ++++++++

    .. list-table::
       :header-rows: 1

       * - Command
         - Description
       * - clean
         - Remove autogenerated folders and artifacts.
       * - clean-pyc
         - Remove python artifacts.
       * - clean-build
         - Remove build artifacts.
       * - bandit
         - Run `bandit`_ security analysis.
       * - mypy
         - Run `mypy`_ type checking.
       * - flake8
         - Run `flake8`_ linting.
       * - install
         - Install all the dependencies and the package itself.
       * - test
         - Run tests and generate coverage report.
       * - build
         - Build wheel package.
       * - publish
         - Publish the built wheel package.

Introduction
------------
{{cookiecutter.short_description}}

User Guide
----------

How to Install
++++++++++++++

Stable release
``````````````

To install {{ cookiecutter.project_name }}, run this command in your terminal:

.. code-block:: console

    $ pip install {{ cookiecutter.project_slug }}

or

.. code-block:: console

    $ poetry self add {{ cookiecutter.project_slug }}

This is the preferred method to install {{ cookiecutter.project_name }}, as it will always install the most recent stable release.


From sources
````````````

The sources for {{ cookiecutter.project_name }} can be downloaded from the `Github repo <{{cookiecutter.project_url}}>`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone {{ cookiecutter.project_url }}.git

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ pip install .

or

.. code-block:: console

    $ poetry install

How to Use
++++++++++

To use {{ cookiecutter.project_name }} in a project::

    import {{ cookiecutter.project_slug }}

Maintainers
-----------

..
    TODO: List here the people responsible for the development and maintaining of this project.
    Format: **Name** - *Role/Responsibility* - Email

* **{{cookiecutter.author}}** - *Maintainer* - `{{cookiecutter.email}} <mailto:{{cookiecutter.email}}?subject=[{{cookiecutter.ci_tool}}]{{ cookiecutter.project_name | replace(" ", "%20") }}>`_