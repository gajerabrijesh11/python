import re
from playwright.sync_api import Page, expect

from Pages.OrangeHRM_pages.hrm_login import HRMLoginPage



def test_hrm_login(page: Page) -> None:
    
    
    login = HRMLoginPage(page)
    
    login.login()
    expect(page).to_have_title("OrangeHRM")