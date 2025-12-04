import re
from playwright.sync_api import Page, expect
from Pages.OrangeHRM_pages.hrm_search_user import test_hrmsystemuserpage
from Pages.OrangeHRM_pages.hrm_login import test_hrmloginpage
from Pages.OrangeHRM_pages.hrm_site_open import test_hrmsiteopenpage

def test_hrm_search_user(page: Page) -> None:
    opensite = test_hrmsiteopenpage(page)
    login = test_hrmloginpage(page)
    search_user = test_hrmsystemuserpage(page)
    opensite.open_site()
    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login()
    search_user.search_user()
    expect(page.get_by_text("Records Found")).to_be_visible()
    
