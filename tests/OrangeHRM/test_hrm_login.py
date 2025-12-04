import re
from playwright.sync_api import Page, expect
from Pages.OrangeHRM_pages.hrm_login import test_hrmloginpage


def test_hrm_login(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login = test_hrmloginpage(page)
    login.enter_username("bgtest")
    login.enter_password("admin123")
    login.click_login()
    expect(page).to_have_title("OrangeHRM")