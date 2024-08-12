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
            "search_bar": self.page.get_by_title("Search"),
            "ul": lambda: self.page.wait_for_selector('xpath=//*[@id="Alh6id"]/div[1]/div/ul'),
            "presentation_locator": self.page.locator("ul[role='listbox'] li div[role='presentation'] span")
        }
    
    def get_locator(self, name: str):
        """
        Retrieves the locator for a given name

        Args:
            name (str): Name of the element to be retrieved
        """
        return self.locators.get(name)
    
