from playwright.sync_api import Page
 
class Locator:
    def __init__(self, page:Page):
        self.page = page

    def login_locator(self):
        return self.page.wait_for_selector('text=Log in')
    
    def dev_login_locator(self):
        return self.page.wait_for_selector('xpath=//*[@id="main"]/article/div/div/div/ul/li[2]/p[2]/a')
    
    def email_locator(self):
        return self.page.get_by_label("Your username or email")
    
    def password_locator(self):
        return self.page.get_by_label("Your password")

    def final_login(self):
        return self.page.get_by_role("button", name="Log in")
    