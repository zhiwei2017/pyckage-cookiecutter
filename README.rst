Pyckage Cookiecutter
====================

.. readthedocs badge
.. image:: https://readthedocs.org/projects/pyckage-cookiecutter/badge/?version=latest
    :target: https://pyckage-cookiecutter.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

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
    :alt: Python 3.7 | Python 3.8 | Python 3.9 | Python 3.10 | Python 3.11

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

Prerequisites
-------------

Please install the Python package cookiecutter_ before using it::

    $ pip install cookiecutter

How to Use
----------

Tutorial
++++++++

Let's pretend you want to create a project called "redditclone".
By using this template based on cookiecutter_,
you will be able to quickly setup a buildable PyPi package.

First, get cookiecutter_. Trust me, it's awesome::

     $ pip install cookiecutter

Now run it against this repo::

     $ cookiecutter https://github.com/zhiwei2017/pyckage-cookiecutter

You'll be prompted for some values. Provide them, then a project will be created for you.

**Warning**: After this point, change 'My Awesome Project', 'John Doe', etc to your own information.

Answer the prompts with your own desired `Prompts <https://pyckage-cookiecutter.readthedocs.io/en/latest/02_prompts.html>`_. For example::

    Cloning into 'pyckage-cookiecutter'...
    remote: Enumerating objects: 219, done.
    remote: Counting objects: 100% (219/219), done.
    remote: Compressing objects: 100% (123/123), done.
    remote: Total 219 (delta 83), reused 181 (delta 69), pack-reused 0
    Receiving objects: 100% (219/219), 41.09 KiB | 1.71 MiB/s, done.
    Resolving deltas: 100% (83/83), done.
    project_name [My Awesome Project]: Reddit Clone
    project_slug [reddit_clone]: reddit
    project_url [https://github.com/example_project]: https://github.com/reddit-clone
    author [John Doe]: John Doe
    email [john-doe@example.com]: john.doe@example.com
    short_description [Behold My Awesome Project!]: A reddit clone.
    version [0.1.0]: 0.1.0
    Select license:
    1 - MIT
    2 - APACHE
    3 - 2-Clause BSD
    4 - 3-Clause BSD
    5 - GPL
    6 - None
    Choose from 1, 2, 3, 4, 5, 6 [1]: 1
    Select ci_tool:
    1 - GitHub
    2 - GitLab
    3 - Bitbucket
    4 - None
    Choose from 1, 2, 3, 4 [1]: 1

Enter the project and take a look around::

    $ cd reddit/
    $ ls

Your repo should have the following structure::

    reddit
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
    ├── reddit
    │   └── version.py                  - version information
    ├── requirements                    - package dependencies
    │   ├── base.txt                    - base dependencies
    │   ├── doc.txt                     - documentation dependencies
    │   └── dev.txt                     - tests dependencies
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
    ├── setup.cfg                       - configurations for mypy, bandit, pytest etc. Centralizing all the configurations to one place.
    └── setup.py                        - package installation configuration

If you want to use CI/CD pipeline for uploading your package to PyPi, please check the section **CI/CD configuration**.

**Note**:

+ This repo is built as a wheel package and uploaded to `PyPi <https://pypi.python.org/pypi/pyckage-cookiecutter/>`_. You can install it through::

    $ pip install pyckage-cookiecutter

  And start generating a new project by call::

    $ pyckage_cookiecutter

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

+-------------+----------------------------------------------+--------------------------------------------------+------------------------------------------------------------------------+
| Config File |          Steps                               |                Trigger Rules                     | Requisite CI/CD Variables                                              |
+=============+==============================================+==================================================+========================================================================+
|             | mypy check                                   |                                                  |                                                                        |
|             +----------------------------------------------+                                                  |                                                                        |
|             | flake8 check                                 | + **Pushes** to *master/develop* branches        |                                                                        |
|             +----------------------------------------------+                                                  |                                                                        |
| test.yml    | bandit check                                 | + **Pull Requests** to *master/develop* branches |                                                                        |
|             +----------------------------------------------+                                                  |                                                                        |
|             | test with python 3.7 (Ubuntu/Mac OS/Windows) |                                                  |                                                                        |
|             +----------------------------------------------+                                                  |                                                                        |
|             | test with python 3.8 (Ubuntu/Mac OS/Windows) |                                                  |                                                                        |
|             +----------------------------------------------+                                                  |                                                                        |
|             | test with python 3.9 (Ubuntu/Mac OS/Windows) |                                                  |                                                                        |
|             +----------------------------------------------+                                                  |                                                                        |
|             | test with python 3.10 (Ubuntu/Mac OS/Windows)|                                                  |                                                                        |
|             +----------------------------------------------+                                                  |                                                                        |
|             | test with python 3.11 (Ubuntu/Mac OS/Windows)|                                                  |                                                                        |
|             +----------------------------------------------+                                                  |                                                                        |
|             | twine check the built package                |                                                  |                                                                        |
+-------------+----------------------------------------------+--------------------------------------------------+------------------------------------------------------------------------+
|             |                                              |                                                  | TWINE_USERNAME                                                         |
| release.yml | deploy to PyPi                               | **Pushes** to tags matching *vXX.XX.XX*          +------------------------------------------------------------------------+
|             |                                              |                                                  | TWINE_PASSWORD                                                         |
+-------------+----------------------------------------------+--------------------------------------------------+------------------------------------------------------------------------+
| sphinx.yml  | deploy GitHub pages                          | **Pushes** to *master* branch                    |                                                                        |
+-------------+----------------------------------------------+--------------------------------------------------+------------------------------------------------------------------------+

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

+-------------+---------------------------------+--------------------------------------------------+------------------------------------------------------------------------+
| Stages      |          Steps                  |                Trigger Rules                     | Requisite CI/CD Variables                                              |
+=============+=================================+==================================================+========================================================================+
|             | mypy check                      |                                                  |                                                                        |
|             +---------------------------------+                                                  |                                                                        |
| linting     | flake8 check                    | + **Pushes** to *master/develop* branches        |                                                                        |
|             +---------------------------------+                                                  |                                                                        |
|             | bandit check                    | + Any **Merge Requests**                         |                                                                        |
+-------------+---------------------------------+                                                  +------------------------------------------------------------------------+
|             | test with python 3.7            |                                                  |                                                                        |
|             +---------------------------------+                                                  |                                                                        |
| test        | test with python 3.8            |                                                  |                                                                        |
|             +---------------------------------+                                                  |                                                                        |
|             | test with python 3.9            |                                                  |                                                                        |
|             +---------------------------------+                                                  |                                                                        |
|             | test with python 3.10           |                                                  |                                                                        |
|             +---------------------------------+                                                  |                                                                        |
|             | test with python 3.11           |                                                  |                                                                        |
+-------------+---------------------------------+                                                  +------------------------------------------------------------------------+
| build       | twine check the built package   |                                                  |                                                                        |
+-------------+---------------------------------+--------------------------------------------------+------------------------------------------------------------------------+
|             |                                 |                                                  | TWINE_USERNAME                                                         |
| deploy      | deploy to PyPi                  | **Pushes** to tags matching *vXX.XX.XX*          +------------------------------------------------------------------------+
|             |                                 |                                                  | TWINE_PASSWORD                                                         |
+-------------+---------------------------------+--------------------------------------------------+------------------------------------------------------------------------+

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

+---------------------------------+--------------------------------------------------+------------------------------------------------------------------------+
|          Steps                  |                Trigger Rules                     | Requisite CI/CD Variables                                              |
+=================================+==================================================+========================================================================+
| mypy check                      |                                                  |                                                                        |
+---------------------------------+                                                  |                                                                        |
| flake8 check                    | + **Pushes** to *master/develop* branches        |                                                                        |
+---------------------------------+                                                  |                                                                        |
| bandit check                    | + Any **Pull Requests**                          |                                                                        |
+---------------------------------+                                                  |                                                                        |
| test with python 3.7            |                                                  |                                                                        |
+---------------------------------+                                                  |                                                                        |
| test with python 3.8            |                                                  |                                                                        |
+---------------------------------+                                                  |                                                                        |
| test with python 3.9            |                                                  |                                                                        |
+---------------------------------+                                                  |                                                                        |
| test with python 3.10           |                                                  |                                                                        |
+---------------------------------+                                                  |                                                                        |
| test with python 3.11           |                                                  |                                                                        |
+---------------------------------+                                                  |                                                                        |
| twine check the built package   |                                                  |                                                                        |
+---------------------------------+--------------------------------------------------+------------------------------------------------------------------------+
|                                 |                                                  | TWINE_USERNAME                                                         |
| deploy to PyPi                  | **Pushes** to tags matching *vXX.XX.XX*          +------------------------------------------------------------------------+
|                                 |                                                  | TWINE_PASSWORD                                                         |
+---------------------------------+--------------------------------------------------+------------------------------------------------------------------------+

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
     - Install and run `bandit`_ security analysis.
   * - mypy
     - Install and run `mypy`_ type checking.
   * - flake8
     - Install and run `flake8`_ linting.
   * - install_requirements
     - Install all the packages listed in txt files in requirements folder.
   * - test
     - Run tests and generate coverage report.
   * - build_whl
     - Build wheel package.

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