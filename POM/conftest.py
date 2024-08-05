import pytest
from playwright.sync_api import sync_playwright

# def pytest_addoption(parser):
#     parser.addoption("--url", action="store", default="https://bing.com", type=str)
#     parser.addoption("--email", action="store", default="Your_email@gmail.com", type=str)
#     parser.addoption("--password", action="store", default="Your_password", type=str)

# @pytest.fixture
# def url(request):
#     return request.config.getoption("--url")

# @pytest.fixture
# def email(request):
#     return request.config.getoption("--email")

# @pytest.fixture
# def password(request):
#     return request.config.getoption("--password")

@pytest.fixture(scope="class")
def setup_and_teardown(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        request.cls.page = page
        request.cls.context = context
        yield page 
        context.close()
        browser.close()

