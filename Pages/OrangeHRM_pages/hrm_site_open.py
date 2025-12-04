from playwright.sync_api import Page
class test_hrmsiteopenpage:
    def __init__(self, page: Page):
        self.page = page
        
    def open_site (self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")