from playwright.sync_api import Page
from Locators.locators import Locator
class googlePage:
    def __init__(self, Page):
        self.page = Page
        self.locator = Locator(Page)

    def search(self, url):

        self.page.goto(url)
        self.locator.search_bar_locator().click()
        self.locator.ul_locator()

        recent_searches = self.locator.presentation_locator().all_text_contents()[:10]

        for index, search in enumerate(recent_searches, start=1):
            print(f"{index}: {search}")

        with open("recent_searches.txt", "w") as file:
            for index, search in enumerate(recent_searches, start=1):
                file.write(f"{index}: {search}\n")

        if len(recent_searches) > 0:
            return True
        else:
            return False
