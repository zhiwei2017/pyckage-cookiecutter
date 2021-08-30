from {{cookiecutter.project_slug}}.version import __version__


class TestVersion:
    def test_version(self):
        assert isinstance(__version__, str)
