import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.hackerrank.com/")
    page.get_by_role("link", name="Log in").click()
    page.get_by_role("link", name="Login").nth(1).click()
    page.get_by_placeholder("Your username or email").click()
    page.get_by_placeholder("Your username or email").fill("eniyank08@gmail.com")
    page.get_by_placeholder("Your password").click()
    page.get_by_placeholder("Your password").fill("Eniyan2002")
    page.get_by_role("button", name="Log In").click()
    page.goto("https://www.hackerrank.com/skills-verification")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
