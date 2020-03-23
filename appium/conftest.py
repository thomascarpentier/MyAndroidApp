# content of conftest.py
import pytest


def pytest_addoption(parser):
    parser.addoption("--apk", action="store", default="", help="full path of apk")


@pytest.fixture
def getAPKPath(request):
    return request.config.getoption("--apk")
