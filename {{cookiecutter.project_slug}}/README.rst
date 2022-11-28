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

Please check the section `Installation <./docs/source/02_installation.rst>`_ for detailed information.

How to Use
++++++++++

Please check the section `Usage <./docs/source/03_usage.rst>`_ for detailed information.

Documentation
+++++++++++++

..
    TODO: update the link to the documentation to your repository.

Maintainers
-----------

..
    TODO: List here the people responsible for the development and maintaining of this project.
    Format: **Name** - *Role/Responsibility* - Email

* **{{cookiecutter.author}}** - *Maintainer* - `{{cookiecutter.email}} <mailto:{{cookiecutter.email}}?subject=[{{cookiecutter.ci_tool}}]{{ cookiecutter.project_name | replace(" ", "%20") }}>`_