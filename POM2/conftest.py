import pytest
from playwright.sync_api import sync_playwright

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