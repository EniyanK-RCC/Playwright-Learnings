import pytest

def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://bing.com", type=str)
    parser.addoption("--email", action="store", default="Your_email@gmail.com", type=str)
    parser.addoption("--password", action="store", default="Your_password", type=str)

@pytest.fixture
def url(request):
    return request.config.getoption("--url")

@pytest.fixture
def email(request):
    return request.config.getoption("--email")

@pytest.fixture
def password(request):
    return request.config.getoption("--password")
