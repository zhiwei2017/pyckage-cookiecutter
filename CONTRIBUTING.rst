Contributing
============

Contributions are welcome, and they are greatly appreciated!

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/zhiwei2017/pyckage-cookiecutter

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the `GitHub <pyckage-cookiecutter>`_ issues for bugs. Anything tagged with **bug**
and **help wanted** is open to whoever wants to implement a fix for it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the `GitHub <pyckage-cookiecutter>`_ issues for features. Anything tagged with **enhancement**
and **help wanted** is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

Pyckage Cookiecutter could always use more documentation, whether as part of
the official docs, in docstrings, or even on the web in blog posts, articles,
and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at
https://github.com/zhiwei2017/pyckage-cookiecutter/issues.

If you are proposing a new feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.

Get Started!
------------

Ready to contribute? Here's how to set up `pyckage-cookiecutter`_ for local
development. Please note this documentation assumes you already have
virtualenv_ and git_ installed and ready to go.

1. Fork the `pyckage-cookiecutter`_ repo on `GitHub <pyckage-cookiecutter>`_.

2. Clone your fork locally:

   .. code-block:: bash

    $ cd path_for_the_repo
    $ git clone git@github.com:YOUR_NAME/pyckage-cookiecutter.git

3. Assuming you have virtualenv_ installed (If you have Python 3.6 this should
   already be there), you can create a new environment for your local
   development by typing:

   .. code-block:: bash

        $ virtualenv pyckage-cookiecutter-venv
        $ source pyckage-cookiecutter-venv/bin/activate

   This should change the shell to look something like:

   .. code-block:: bash

        (pyckage-cookiecutter-env) $

4. Create a branch for local development:

   .. code-block:: bash

        $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. The next step would be to run the test cases:

   .. code-block:: bash

        $ make test

6. Before raising a pull request you should also run tox. This will run the
   tests across different versions of Python:

   .. code-block:: bash

        $ tox

   If you are missing pytest and/or tox, just `poetry install` them into
   your virtual environment.

7. If your contribution is a bug fix or new feature, you may want to add a test
   to the existing test suite. See section Add a New Test below for details.

8. Commit your changes and push your branch to `GitHub <pyckage-cookiecutter>`_:

   .. code-block:: bash

        $ git add .
        $ git commit -m "Your detailed description of your changes."
        $ git push origin name-of-your-bugfix-or-feature

10. Submit a pull request through the `GitHub <pyckage-cookiecutter>`_ website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.

2. If the pull request adds functionality, the docs should be updated. Put your
   new functionality into a function with a docstring.

3. The pull request should work for Python 3.8, 3.9, 3.10 and 3.11.

Add a New Test
--------------

When fixing a bug or adding features, it's good practice to add a test to
demonstrate your fix or new feature behaves as expected. These tests should
focus on one tiny bit of functionality and prove changes are correct.

To write and run your new test, follow these steps:

1. Add the new test to `tests/test_bake_project.py`. Focus your test on the
   specific bug or a small part of the new feature.

2. Run your test and confirm that your test does not fail:

   .. code-block:: bash

        $ make test

3. Run the tests with tox to ensure that the code changes work with
   different Python versions:

   .. code-block:: bash

        $ tox

Deploying
---------

To deploy the package, just run::

    $ poetry version patch  # possible: major / minor / patch / premajor / preminor / prepatch / prerelease
    $ git commit -m "Bump version: <old_version> -> <new_version>" 
    $ git push
    $ git push --tags

Github Actions will do the rest.

.. _virtualenv: https://virtualenv.pypa.io/en/stable/installation
.. _git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
.. _pyckage-cookiecutter: https://github.com/zhiwei2017/pyckage-cookiecutter
