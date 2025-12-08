from playwright.sync_api import Page
class HRMLoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.hrmuser_input = page.get_by_role("textbox", name="Username")
        self.hrmpassword_input = page.get_by_role("textbox", name="Password")
        self.hrmlogin_button = page.get_by_role("button", name="Login")
    def enter_username (self, username):
        self.hrmuser_input.fill(username)
        # self.enter_username("Admin")
    def enter_password (self, password):
        self.hrmpassword_input.fill(password)
        # self.enter_password("admin123")
    def click_login (self):
        self.hrmlogin_button.click()