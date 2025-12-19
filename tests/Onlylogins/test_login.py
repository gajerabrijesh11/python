import re
from playwright.sync_api import Page, expect
from Pages.Onlylogins_Page.Only_Login import test_Only_LoginPage


def test_Valid_login(page: Page) -> None:
    page.goto("https://practicetestautomation.com/practice-test-login/")
    login = test_Only_LoginPage(page)
    logout = test_Only_LoginPage(page)
    login.enter_username("student")
    login.enter_password("Password123")
    login.click_login()
    expect(page.get_by_text("Congratulations student. You")).to_be_visible()
    logout.click_logout()
    

def test_Wrong_user(page: Page) -> None:
    page.goto("https://practicetestautomation.com/practice-test-login/")
    login = test_Only_LoginPage(page)
    logout = test_Only_LoginPage(page)
    login.enter_username("studnt")
    login.enter_password("Password123")
    login.click_login()
    expect(page.locator("#error")).to_be_visible()

def test_Wrong_password(page: Page) -> None:
    page.goto("https://practicetestautomation.com/practice-test-login/")
    login = test_Only_LoginPage(page)
    logout = test_Only_LoginPage(page)
    login.enter_username("student")
    login.enter_password("password123")
    login.click_login()
    expect(page.locator("#error")).to_be_visible()
