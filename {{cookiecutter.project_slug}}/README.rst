{{cookiecutter.project_name}}
{% for _ in cookiecutter.project_name %}={% endfor %}

Introduction
------------
{{cookiecutter.short_description}}

Prerequisites
-------------
To install the dependencies listed in `requirements/base.txt`, you can use::

    $ pip install -r requirements/base.txt

User Guide
----------

How to Install
++++++++++++++

Stable release
``````````````

To install {{ cookiecutter.project_name }}, run this command in your terminal:

.. code-block:: console

    $ pip install {{ cookiecutter.project_slug }}

This is the preferred method to install {{ cookiecutter.project_name }}, as it will always install the most recent stable release.


From sources
````````````

The sources for {{ cookiecutter.project_name }} can be downloaded from the `Github repo <{{cookiecutter.project_url}}>`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone {{ cookiecutter.project_url }}.git

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install

or

.. code-block:: console

    $ pip install .

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