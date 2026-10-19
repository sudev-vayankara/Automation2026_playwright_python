import pytest
@pytest.mark.asyncio
async def test_end_to_end(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/")

    # =============================================================================
    # ====================== Reg
    # =================================================================================
    await async_page.locator("//a[text()='Register']").click()
    await async_page.get_by_label("First name:").fill("abc")
    await async_page.get_by_label("Last name:").fill("abc")
    await async_page.get_by_label("Email:").fill("abcd12345@gmail.com")
    await async_page.get_by_label("Password:").nth(0).fill("abc@12345")
    await async_page.get_by_label("Confirm password:").fill("abc@12345")
    await async_page.locator("#register-button").click()

    try:
        await async_page.get_by_text("Log out").is_visible()

    except Exception:
          print(await async_page.locator("//span[@class='field-validation-error']").all_text_contents())

    # =============================================================================
    # ====================== login
    # =================================================================================
    await async_page.get_by_text("Log in").click()
    await async_page.get_by_label("Email:").fill("roshitha.s@benzyinfotech.com")
    await async_page.get_by_label("Password:").fill("sara123*")
    await async_page.locator("//input[@value='Log in']").click()
    try:
        await async_page.get_by_text("Log out").is_visible()

    except Exception:
        print(await async_page.locator("//span[@class='field-validation-error']").all_text_contents())
#  ============================================================================================
#   =================== SEARCH
# ==============================================================================================
#     await async_page.locator("#small-searchterms").fill("COMPUTER")
    await async_page.locator("(//a[contains(text(),'Books')])[3]").click()
    product_name = ["Computing and Internet","Fiction"]
    for i in product_name:
        await async_page.locator(f"//a[text()='{i}']/../..//input[@value='Add to cart']").click()
    await async_page.locator("//span[text()='Shopping cart']").click()

#=================================================================================
#                                   order
# ================================================================================

    await async_page.locator("//span[text()='Shopping cart']").click()
    await async_page.locator("#termsofservice").click()
    await async_page.locator("#checkout").click()

# =================================================================================
#               order
# ==================================================================================
    ele =    async_page.locator("#BillingNewAddress_CountryId")
    await  ele.select_option(label="India")
    await async_page.locator("#BillingNewAddress_City").fill("Mysore")
    await async_page.locator("#BillingNewAddress_Address1").fill("srinagar")
    await async_page.locator("#BillingNewAddress_ZipPostalCode").fill("502561")
    await async_page.locator("#BillingNewAddress_PhoneNumber").fill("123456798")

    await async_page.locator("(//input[@title='Continue'])[1]").click()
    await async_page.locator("(//input[@title='Continue'])[2]").click()
    await async_page.locator("(//input[@title='Continue'])[3]").click()
    await async_page.locator("(//input[@type='button'])[5]").click()
    await async_page.locator("(//input[@type='button'])[6]").click()
    await async_page.locator("(//input[@type='button'])[7]").click()
# ============================================================================
#
# ============================================================================