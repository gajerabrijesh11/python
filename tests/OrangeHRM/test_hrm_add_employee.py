import re
from playwright.sync_api import Page, expect

from Pages.OrangeHRM_pages.hrm_login import HRMLoginPage
from Pages.OrangeHRM_pages.hrm_site_open import HRMSiteOpenPage
from Pages.OrangeHRM_pages.hrm_add_employee import HRMAddEmployeePage

def test_hrm_add_employee(page: Page) -> None:
    opensite = HRMSiteOpenPage(page)
    login = HRMLoginPage(page)
    addemployee = HRMAddEmployeePage(page)
    deleteemployee = HRMAddEmployeePage(page)
    opensite.open_site()
    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login()
    addemployee.add_employee()
    expect(page.get_by_role("heading", name="B N")).to_be_visible()
    deleteemployee.delete_employee()
