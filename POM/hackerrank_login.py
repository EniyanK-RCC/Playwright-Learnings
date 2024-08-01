from playwright.sync_api import Page

class Hackerrank_Login:
    def __init__(self, page: Page):
        self.page = page
        self.username_or_email_textbox = page.get_by_placeholder("Your username or email")
        self.password_textbox = page.get_by_placeholder("Your password")
        self.login_button = page.get_by_role("button", name="Log In")

    def login_page(self, url):
        self.page.goto(url)
        self.page.get_by_role("link", name="Log in").click()
        self.page.get_by_role("link", name="Login").nth(1).click()

    def login(self, username_or_email, password):
        self.username_or_email_textbox.fill(username_or_email)
        self.password_textbox.fill(password)
        self.login_button.click()