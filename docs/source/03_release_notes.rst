Release Notes
=============

Versioning
----------


We use `SemVer <http://semver.org/>`_ for versioning. For the versions available, see the `the project tags <https://github.com/KnightConan/pyckage-cookiecutter/tags>`_.

0.1.0
-----

Welcome to **0.1.0** release, which is now at the master branch in the Gitlab repository at `Pyckage Cookiecutter <https://github.com/KnightConan/pyckage-cookiecutter>`_

*Features:*
  * Introduces #1: Initial implementation of pyckage cookiecutter.

0.1.1
-----

*Features:*
  * Introduces #1:

    * Requirements rearrangement:

      1. create requirements folder for containing requirements files
      2. move requirements.txt to base.txt in requirements folder, requirements-docs.txt to doc.txt in requirements folder, 3. 3. requirements-tests.txt to dev.txt in requirements folder
      3. add dependency file base.txt in doc.txt and dev.txt
      4. adapt changes to corresponding files, such as Makefile, README.rst, pipeline files, setup.py etc
      5. remove redundant dependencies in dev.txt and pyproject.toml
      6. Update Makefile to have 'python -m' as prefix for all pip commands to keep it consistent
      7. update test_bake_project.py with make commands for executing tests for linting and pytest

    * Bug fix:

      1. fix Wrong README file type in package setup.py
      2. fix muted failed version import in setup.py
      3. fix broken setup.py because of requirements rearrangement