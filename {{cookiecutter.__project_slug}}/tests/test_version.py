import importlib.metadata


def test_version():
    assert isinstance(importlib.metadata.version("{{cookiecutter.__project_slug}}"), str)
