from playwright.sync_api import Page
class test_Only_LoginPage:
    def __init__(self, page: Page):
        self.page = Page
        self.usename_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Submit")
        self.logout_button = page.get_by_role("link", name="Log out")
    def enter_username (self, username):
        self.usename_input.fill(username)
        
    def enter_password (self, password):
        self.password_input.fill(password)
        
    def click_login (self):
        self.login_button.click()
    def click_logout (self):
        self.logout_button.click()