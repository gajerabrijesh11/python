import re
from playwright.sync_api import Page, expect

from Pages.OrangeHRM_pages.hrm_login import HRMLoginPage

from Pages.OrangeHRM_pages.hrm_add_employee import HRMAddEmployeePage

def test_hrm_add_employee(page: Page) -> None:
    
    login = HRMLoginPage(page)
    addemployee = HRMAddEmployeePage(page)
    deleteemployee = HRMAddEmployeePage(page)
    
    login.login()
    
    addemployee.add_employee()
    page.get_by_role("heading", name="B N").wait_for(state="visible")
    expect(page.get_by_role("heading", name="B N")).to_be_visible
    deleteemployee.delete_employee()
