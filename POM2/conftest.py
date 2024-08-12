import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="class")
def setup_and_teardown(request):
    """
    A pytest fixture for setting up and tearing down a Playwright browser session.

    Args:
        request: Pytest request object, which provide information about requesting test context.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        request.cls.page = page
        yield
        browser.close()