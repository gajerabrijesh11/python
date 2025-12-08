from playwright.sync_api import Page
class HRMSystemUserPage:
    def __init__(self, page: Page):
        self.page = page
        
    def search_user (self):
        self.page.get_by_role("link", name="Admin").click()
    