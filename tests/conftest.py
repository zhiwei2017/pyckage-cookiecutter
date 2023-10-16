import itertools
import pytest
from collections import OrderedDict


def generate_supported_combinations(OPTIONS, UNSUPPORTED_COMBINATIONS):
    def is_contained(option, unspported_options):
        for us in unspported_options:
            return option.intersection(us) == us
    result = []
    unspported = [set(combi.items()) for combi in UNSUPPORTED_COMBINATIONS]
    for values in itertools.product(*OPTIONS.values()):
        if is_contained(set(zip(OPTIONS.keys(), values)), unspported):
            continue
        result.append(dict(zip(OPTIONS.keys(), values)))
    return result


def pytest_configure():
    pytest.OPTIONS = OrderedDict([
        ("ci_tool", ["GitLab", "GitHub", "Bitbucket", "None"]),
        ("license", ["MIT", "APACHE", "2-Clause BSD", "3-Clause BSD", "GPL", "None"])
    ])
    pytest.UNSUPPORTED_COMBINATIONS = []
    pytest.SUPPORTED_COMBINATIONS = generate_supported_combinations(
        pytest.OPTIONS, pytest.UNSUPPORTED_COMBINATIONS)



@pytest.fixture
def context():
    return {
        "author": "Test Author",
        "email": "test@example.com",
        "project_name": "My Test Project",
        "__project_slug": "my_test_project",
        "project_url": "https:/dummy.com/my_test_project",
        "short_description": "A short description of the project.",
        "version": "0.1.0"
    }
