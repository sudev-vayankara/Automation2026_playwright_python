import pytest

@pytest.mark.asyncio
async def test_mul_wiind(async_page):
    await async_page.goto("https://www.amazon.in/")
    
    search_box = async_page.locator("#twotabsearchtextbox")
    await search_box.fill("Books")
    await search_box.press("Enter")
    
    # Wait for search results to load properly instead of a fixed timeout
    books = async_page.locator("h2.a-size-medium.a-spacing-none.a-color-base.a-text-normal")
    await books.first.wait_for(state="visible")

    # Handle the first product click (if it opens a new tab/window)
    async with async_page.expect_popup() as pop_info:
        await books.first.click()

    product_page = await pop_info.value
    await product_page.wait_for_load_state("domcontentloaded")

    # Click 'Add to Cart' (stays on the same product page or opens a side sheet)
    add_to_cart_btn = product_page.locator("//input[@id='add-to-cart-button']")
    await add_to_cart_btn.click()

    # Wait for the cart confirmation / side panel / elements to update
    # If Amazon prompts a specific cart sub-page or "Proceed to Checkout" button:
    checkout_button = product_page.locator("//input[@name='proceedToRetailCheckout' or @data-feature-id='proceed-to-checkout-action']")
    await checkout_button.wait_for(state="visible")
    await checkout_button.click()