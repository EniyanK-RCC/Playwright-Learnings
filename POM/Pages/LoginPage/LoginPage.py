from playwright.sync_api import Page
from Locators.locators import Locator

class Hackerrank_Login_Page:
    def __init__(self, page: Page):
        self.page = page
        self.locator = Locator(page)

    def login(self, username_or_email, password):
        self.locator.email_locator().fill(username_or_email)
        self.locator.password_locator().fill(password)
        self.locator.final_login().click()