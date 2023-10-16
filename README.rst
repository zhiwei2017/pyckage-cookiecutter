Pyckage Cookiecutter
====================

.. actions building badge
.. image:: https://github.com/zhiwei2017/pyckage-cookiecutter/workflows/Unit%20Test%20&%20Build%20Test/badge.svg
    :target: https://github.com/zhiwei2017/pyckage-cookiecutter/actions

.. pypi version badge
.. image:: https://img.shields.io/pypi/v/pyckage-cookiecutter.svg
    :target: https://pypi.python.org/pypi/pyckage-cookiecutter/

.. license badge
.. image:: https://img.shields.io/pypi/l/pyckage-cookiecutter.svg
    :target: https://pypi.python.org/pypi/pyckage-cookiecutter/

.. python version badge from PyPI
.. image:: https://img.shields.io/pypi/pyversions/pyckage-cookiecutter.svg
    :target: https://pypi.python.org/pypi/pyckage-cookiecutter/
    :alt: Python 3.8 | Python 3.9 | Python 3.10 | Python 3.11 | Python 3.12

.. pypi format
.. image:: https://img.shields.io/pypi/format/pyckage-cookiecutter.svg
    :target: https://badge.fury.io/py/pyckage-cookiecutter

Introduction
------------

This projects consist of a cookiecutter_
template that generates a full structure for a creating a PyPi standard package.

While using this project, you will be asked to provide some inputs such as the author,
the name of the project, etc. As result you will obtain the
complete file and folder structure to quickly start to code your package.

How to Use
----------

Tutorial
++++++++

Let's pretend you want to create a project called "feddit".
By using this template based on cookiecutter_,
you will be able to quickly setup a buildable PyPi package.

First, get cookiecutter_. Trust me, it's awesome::

     $ pip install cookiecutter

or with **poetry**::

     $ poetry self add cookiecutter

Now run it against this repo::

     $ cookiecutter https://github.com/zhiwei2017/pyckage-cookiecutter
     
or::

    $ poetry run cookiecutter https://github.com/zhiwei2017/pyckage-cookiecutter

You'll be prompted for some values. Provide them, then a project will be created for you.

**Warning**: After this point, change '*My Awesome Project*', '*John Doe*', etc to your own information.

Answer the prompts with your own desired `Prompts <https://zhiwei2017.github.io/pyckage-cookiecutter/02_prompts.html>`_. For example::

    Cloning into 'pyckage-cookiecutter'...
    remote: Enumerating objects: 219, done.
    remote: Counting objects: 100% (219/219), done.
    remote: Compressing objects: 100% (123/123), done.
    remote: Total 219 (delta 83), reused 181 (delta 69), pack-reused 0
    Receiving objects: 100% (219/219), 41.09 KiB | 1.71 MiB/s, done.
    Resolving deltas: 100% (83/83), done.
      [1/8] Select your project name (My Awesome Project):
      [2/8] Project URL for hosting the source code. (https://repository-hosting.com/example_project): https://github.com/zhiwei2017/feddit
      [3/8] Author full name. (John Doe): John Doe
      [4/8] Author email address. (john.doe@email.com): john.doe@example.com
      [5/8] Short description. (Behold My Awesome Project!): A fake reddit API.
      [6/8] Semantic version to use for release. (0.1.0): 0.1.0
      [7/8] Which license do you want to use for your project?
        1 - None
        2 - MIT
        3 - APACHE
        4 - 2-Clause BSD
        5 - 3-Clause BSD
        6 - GPL
        Choose from [1/2/3/4/5/6] (1): 2
      [8/8] Which CI/CD pipelines do you plan to use?
        1 - None
        2 - GitHub
        3 - GitLab
        4 - Bitbucket
        Choose from [1/2/3/4] (1): 2
    **Please read the comments from README.rst in your project to get to know how to setup the CI/CD pipeline and use commands from Makefile.**

Enter the project and take a look around::

    $ cd feddit/
    $ ls

Your repo should have the following structure::

    feddit
    ├── .github                         - github actions configurations
    │   └── workflows
    │       ├── test.yml                - pipelines for linting checks and testing
    │       ├── release.yml             - pipelines for releases with tags
    │       └── sphinx.yml              - pipelines for publishing github pages
    ├── docs                            - sphinx documentation
    │   ├── Makefile                    - Makefile defines terminal commands for sphinx documentation
    │   └── source                      - documentation source folder
    │       ├── 01_about.rst
    │       ├── 02_source.rst
    │       ├── 03_authors.rst
    │       ├── 04_contributing.rst
    │       ├── conf.py                 - sphinx configuration file
    │       └── index.rst
    ├── feddit
    │   └── __init__.py
    ├── tests                           - tests
    │   ├── resources                   - resources used in tests
    │   ├── conftest.py                 - fixtures in tests
    │   └── test_version.py             - test version information.
    ├── .gitignore
    ├── CONTRIBUTING.rst                - contributing guidelines
    ├── LICENSE
    ├── Makefile                        - predefined terminal commands
    ├── MANIFEST.in                     - commands, one per line, instructing setuptools to add or remove some set of files from the sdis
    ├── README.rst                      - package information
    ├── setup.cfg                       - configurations for flake8, since it doesn't support pyproject.toml.
    └── pyproject.toml                  - package configuration file

If you want to use CI/CD pipeline for uploading your package to PyPi, please check the section **CI/CD configuration**.

**Note**:

+ This repo is built as a wheel package and uploaded to `PyPi <https://pypi.python.org/pypi/pyckage-cookiecutter/>`_. You can install it through **pip**::

    $ pip install pyckage-cookiecutter

  or through **poetry**::

    $ poetry self add pyckage-cookiecutter

  And start generating a new project by call::

    $ pyckage_cookiecutter
  
  or::

    $ poetry run pyckage_cookiecutter

  The rest is the same as the `Tutorial <#tutorial>`_ introduced.

CI/CD Pipelines
+++++++++++++++

The CI/CD pipelines are predefined in the generated project. Please check following sections for
which steps are included and how to configure them in different platforms.

GitHub Actions
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
|             | test with python 3.12 (Ubuntu/Mac OS/Windows)|                                                  |                             |                                                           |
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

GitLab CI
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
|         +---------------------------------+                                           |                              |                                                           |
|         | test with python 3.12           |                                           |                              |                                                           |
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

Bitbucket Pipelines
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
| test with python 3.12           |                                           |                              |                                                           |
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

Acknowledgements
----------------

Special thanks to the project `cookiecutter-pypackage <https://github.com/audreyfeldroy/cookiecutter-pypackage>`_ for the nice *CONTRIBUTING.rst* template.

Author
------

* `Zhiwei Zhang <https://github.com/zhiwei2017>`_ - *Author* / *Maintainer* - `zhiwei2017@gmail.com <mailto:zhiwei2017@gmail.com?subject=[GitHub]Pyckage%20Cookiecutter>`_


.. _bandit: https://bandit.readthedocs.io/en/latest/
.. _mypy: https://github.com/python/mypy
.. _flake8: https://gitlab.com/pycqa/flake8
.. _pytest: https://docs.pytest.org/en/stable/
.. _cookiecutter: https://github.com/cookiecutter/cookiecutter
.. _pyckage-cookiecutter: https://github.com/zhiwei2017/pyckage-cookiecutter