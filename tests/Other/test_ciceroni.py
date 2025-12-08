from playwright.sync_api import Page, expect

def test_checkcart(page):
    page.goto("https://ciceroni.in/")
    page.get_by_label("Marketing offer form").get_by_role("button", name="Close").click()
    page.get_by_role("link", name="Cart").click()
    expect(page.get_by_text("Your cart is empty")).to_be_visible()
    
"""""
def test_addtocart(page: Page):
    page.goto("https://ciceroni.in/")
    page.get_by_label("Marketing offer form").get_by_role("button", name="Close").click()
    page.get_by_role("link", name="Men", exact=True).hover()
    page.locator("div:has-text('TOPWEAR')").get_by_role("link", name="Tee-Shirt").click()
    
    card = page.locator("div", has_text="Matsya").first
    card.scroll_into_view_if_needed()
    card.wait_for(state="visible")
    card.hover()
    try:
     card.locator("a.quickbuy-toggle:has-text('Quick buy')").first.click() 
     print("Quick buy clicked")
    except:
     print("Quick buy not clicked")
    page.locator(".option-selector__btns > label:nth-child(8)").click()
    
    try:
     plus_btn = page.get_by_role("link", name="Increase quantity")
     for i in range(4):
      plus_btn.click()
     print("Item added")
    except:
      print("not added")
    page.get_by_role("button", name="Add to cart").click()
    expect (page.locator("a.cart-link__count:has-text(1)")).to_be_visible()
    # expect(page.get_by_text("Size: L")).to_have_text("Size: L")
    # expect(page.get_by_role("dialog", name="Your cart (5)").get_by_label("Quantity", exact=True)).to_have_text("Your cart (5)")
    """