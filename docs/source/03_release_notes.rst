Release Notes
=============

Versioning
----------


We use `SemVer <http://semver.org/>`_ for versioning. For the versions available, see the `the project tags <https://github.com/zhiwei2017/pyckage-cookiecutter/tags>`_.

0.1.0
-----

Welcome to **0.1.0** release, which is now at the master branch in the Gitlab repository at `Pyckage Cookiecutter <https://github.com/zhiwei2017/pyckage-cookiecutter>`_

*Features:*

* Introduces `#1 <https://github.com/zhiwei2017/pyckage-cookiecutter/pull/1>`_: Initial implementation of pyckage cookiecutter.

0.1.1
-----

*Features:*

* Introduces `#2 <https://github.com/zhiwei2017/pyckage-cookiecutter/pull/2>`_:

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

0.2.0
-----
*Features:*

* Introduces `#4 <https://github.com/zhiwei2017/pyckage-cookiecutter/pull/4>`_:

  + Update documentation for release notes
  + Add more tags in ``pyproject.toml``

* Introduces `#5 <https://github.com/zhiwei2017/pyckage-cookiecutter/pull/5>`_:

  + Add sphinx.yml for github pages publishing
  + Adjust documentation in ``README.rst`` for how to setup CI/CD pipelines in different platforms
  + Add Acknowledgements section in ``README.rst``

* Introduces `#7 <https://github.com/zhiwei2017/pyckage-cookiecutter/pull/7>`_:

  + Add twine check in ``test_bake_project.py`` and github actions for pull requests or pushes to master/develop branches
  + Add twine check step in all pipelines in the cookiecutter template
  + Update corresponding section in ``README.rst`` at root and adapt ``README.rst`` with additional configuration information for pipelines
  + Add missing linting checks in github actions file in cookiecutter template
  + Add whl file extension for twine upload