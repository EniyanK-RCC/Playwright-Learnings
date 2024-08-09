from playwright.sync_api import Page
 
class Locator:
    def __init__(self, page:Page):
        self.page = page

    def search_bar_locator(self):
        return self.page.get_by_title("Search")
    
    def ul_locator(self):
        return self.page.wait_for_selector('xpath=//*[@id="Alh6id"]/div[1]/div/ul')
    
    def presentation_locator(self):
        return self.page.locator("ul[role='listbox'] li div[role='presentation'] span")