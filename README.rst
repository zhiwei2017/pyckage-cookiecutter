Pyckage Cookiecutter
====================

.. readthedocs badge
.. image:: https://readthedocs.org/projects/pyckage-cookiecutter/badge/?version=latest
    :target: https://pyckage-cookiecutter.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. actions building badge
.. image:: https://github.com/KnightConan/pyckage-cookiecutter/workflows/Unit%20Test%20&%20Build%20Test/badge.svg
    :target: https://github.com/KnightConan/pyckage-cookiecutter/actions

.. pypi version badge
.. image:: https://img.shields.io/pypi/v/pyckage-cookiecutter.svg
    :target: https://pypi.python.org/pypi/pyckage-cookiecutter/

.. license badge
.. image:: https://img.shields.io/pypi/l/pyckage-cookiecutter.svg
    :target: https://pypi.python.org/pypi/pyckage-cookiecutter/

.. python version badge from PyPI
.. image:: https://img.shields.io/pypi/pyversions/pyckage-cookiecutter.svg
    :target: https://pypi.python.org/pypi/pyckage-cookiecutter/
    :alt: Python 3.6 | Python 3.7 | Python 3.8 | Python 3.9

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

     $ cookiecutter https://github.com/KnightConan/pyckage-cookiecutter

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
    author [John Doe]: John Doe
    email [john-doe@example.com]: john.doe@example.com
    project_name [My Awesome Project]: Reddit Clone
    project_slug [reddit_clone]: reddit
    project_url [https://github.com/example_project]: https://github.com/reddit-clone
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
    │       ├── main.yml                - pipelines for master, develop and pull requests
    │       └── release.yml             - pipelines for release with tags
    ├── docs                            - sphinx documentation
    │   ├── Makefile                    - Makefile defines terminal commands for sphinx documentation
    │   └── source                      - documentation source folder
    │       ├── 01_about.rst
    │       ├── 02_installation.rst
    │       ├── 03_usage.rst
    │       ├── 04_source.rst
    │       ├── 05_release_notes.rst
    │       ├── 06_authors.rst
    │       ├── 07_contributing.rst
    │       ├── conf.py                 - sphinx configuration file
    │       └── index.rst
    ├── reddit
    │   └── version.py                  - version information
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
    ├── requirements                    - package dependencies
    │   ├── base.txt                    - base dependencies
    │   ├── doc.txt                     - documentation dependencies
    │   └── dev.txt                     - tests dependencies
    ├── setup.cfg                       - configurations for mypy, bandit, pytest etc. Centralizing all the configurations to one place.
    ├── setup.py                        - package installation configuration
    └── tox.ini                         - run tests with multiple python versions

If you want to use CI/CD pipeline for uploading your package to PyPi, please check the section **CI/CD configuration**.

**Note**:

+ This repo is built as a wheel package and uploaded to `PyPi <https://pypi.python.org/pypi/pyckage-cookiecutter/>`_. You can install it through::

    $ pip install pyckage-cookiecutter

  And start generating a new project by call::

    $ pyckage_cookiecutter

  The rest is the same as the `Tutorial <#tutorial>`_ introduced.

CI/CD configuration
+++++++++++++++++++

Following steps are predefined in the CI/CD pipelines:

+ mypy check
+ flake8 check
+ bandit check
+ test with python 3.6
+ test with python 3.7
+ test with python 3.8
+ deploy to PyPi

Three CI/CD Variables are requisite for the step **deploy to PyPi**:

* TWINE_USERNAME
* TWINE_PASSWORD
* TWINE_REPOSITORY_URL

  + https://test.pypi.org/legacy/ for uploading to test version PyPi
  + https://upload.pypi.org/legacy/ for uploading to official PyPi

For how to set CI/CD variables in different platform, please reference the following table:

.. list-table::
   :header-rows: 1

   * - Platform
     - Setup Steps
   * - Github
     - Settings -> Secrets -> New repository secret
   * - GitLab
     - Settings -> CI/CD -> Variables -> Add variable
   * - Bitbucket
     - Repository settings -> Repository variables -> add

Author
------

* `Zhiwei Zhang <https://github.com/KnightConan>`_ - *Author* / *Maintainer* - `zhiwei2017@gmail.com <mailto:zhiwei2017@gmail.com?subject=[GitHub]Pyckage%20Cookiecutter>`_


.. _cookiecutter: https://github.com/cookiecutter/cookiecutter
.. _pyckage-cookiecutter: https://github.com/KnightConan/pyckage-cookiecutter