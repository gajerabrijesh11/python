import re
from playwright.sync_api import Page, expect
from Pages.Other_pages.login import test_loginpage
from Pages.Other_pages.addtocart import test_addtocartpage
from Pages.Other_pages.logout import test_logoutpage

def test_POM_POC(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    login = test_loginpage(page)
    addtocart = test_addtocartpage(page)
    logout = test_logoutpage(page)
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()
    addtocart.addtocart()
    addtocart.addtocardvisible()
    logout.openmenu()
    logout.logout()
    logout.logoutdone()

def test_locked_out_user(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    login = test_loginpage(page)
    login.enter_username("locked_out_user")
    login.enter_password("secret_sauce")
    login.click_login()
    if expect(page.locator("[data-test=\"error\"]")).to_be_visible():
     print("user locked out")
    else:
     print("if condition failed")
