from playwright.sync_api import Page, expect
class test_logoutpage:
    def __init__(self, page: Page):
        self.page = Page
        self.open_menu = page.get_by_role("button", name="Open Menu")
        self.logout_button = page.locator("[data-test=\"logout-sidebar-link\"]")
        self.logout_validate = page.get_by_text("Swag Labs")
    def openmenu (self):
        self.open_menu.click()
    def logout (self):
        self.logout_button.click()
    def logoutdone (self):
        return self.logout_validate.is_visible()