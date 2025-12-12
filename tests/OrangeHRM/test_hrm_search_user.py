import re
from playwright.sync_api import Page, expect
from Pages.OrangeHRM_pages.hrm_search_user import HRMSystemUserPage
from Pages.OrangeHRM_pages.hrm_login import HRMLoginPage


def test_hrm_search_user(page: Page) -> None:
    
    login = HRMLoginPage(page)
    search_user = HRMSystemUserPage(page)
    
    login.login()
    search_user.search_user()
    expect(page.get_by_text("Records Found")).to_be_visible()
    
