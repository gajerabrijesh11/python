from playwright.sync_api import Page, expect
class test_addtocartpage:
    def __init__(self, page: Page):
        self.page = Page
        self.addtocart_button = page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")
        self.addtocart_visible = page.locator("[data-test=\"shopping-cart-link\"]")
    def addtocart (self):
        self.addtocart_button.click()
        
    def addtocardvisible (self):
        return self.addtocart_visible.is_visible()