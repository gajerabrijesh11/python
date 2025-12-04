import re
from playwright.sync_api import Page, expect

from Pages.OrangeHRM_pages.hrm_login import test_hrmloginpage
from Pages.OrangeHRM_pages.hrm_site_open import test_hrmsiteopenpage
from Pages.OrangeHRM_pages.hrm_add_employee import test_hrmaddemployeepage

def test_hrm_add_employee(page: Page) -> None:
    opensite = test_hrmsiteopenpage(page)
    login = test_hrmloginpage(page)
    addemployee = test_hrmaddemployeepage(page)
    deleteemployee = test_hrmaddemployeepage(page)
    opensite.open_site()
    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login()
    addemployee.add_employee()
    expect(page.get_by_role("heading", name="B N")).to_be_visible()
    deleteemployee.delete_employee()
