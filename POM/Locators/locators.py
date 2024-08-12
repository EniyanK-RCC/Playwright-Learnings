from playwright.sync_api import Page
 
class Locator:
    """
    A locator class for retrieving locators for elements in a web page
    """
    def __init__(self, page:Page):
        """
        Initializes the locator class with page instance and defines the locators

        Args:
            page (Page): The playwright page object representing the browser page
        """
        self.page = page
        self.locators = {
            "login_locator": lambda: self.page.wait_for_selector('text=Log in'),
            "dev_login_locator": lambda: self.page.wait_for_selector('xpath=//*[@id="main"]/article/div/div/div/ul/li[2]/p[2]/a'),
            "email_locator": self.page.get_by_label("Your username or email"),
            "password_locator": self.page.get_by_label("Your password"),
            "final_login": self.page.get_by_role("button", name="Log in")
        }

    def get_locator(self, name: str):
        """
        Retrieves the locator for a given name

        Args:
            name (str): Name of the element to be retrieved
        """
        return self.locators.get(name)
    