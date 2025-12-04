from playwright.sync_api import Page
class test_loginpage:
    def __init__(self, page: Page):
        self.page = Page
        self.usename_input = page.locator("[data-test=\"username\"]")
        self.password_input = page.locator("[data-test=\"password\"]")
        self.login_button = page.locator("[data-test=\"login-button\"]")
    def enter_username (self, username):
        self.usename_input.fill(username)
    def enter_password (self, password):
        self.password_input.fill(password)
    def click_login (self):
        self.login_button.click()