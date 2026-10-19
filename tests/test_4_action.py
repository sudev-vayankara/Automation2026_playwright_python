import pytest
@pytest.mark.asyncio
async def test_ele_methods(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/")
    ele =  async_page.get_by_text("Register")
    text_of_ele = await ele.inner_text()
    print("text of the ele is inner text" ,text_of_ele)
    text_of_ele = await ele.inner_html()
    print("text of the ele is html text", text_of_ele)
    text_of_ele = await ele.text_content()
    print("text of the ele is text content ", text_of_ele)

    #get attribute
    href = await ele.get_attribute("href")
    print("get href attribute value is ", href)
    class_ = await ele.get_attribute("class")
    print("get class attribute value is ", class_)


@pytest.mark.asyncio
async def test_mul_ele_methods(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/")
    products = async_page.locator("//h2[@class='product-title']")
    print(products)
    # await products.first.click()
    # await async_page.wait_for_timeout(5000)
    # await products.last.click()
    # await async_page.wait_for_timeout(5000)
    await products.nth(1).click()
    await async_page.wait_for_timeout(5000)


@pytest.mark.asyncio
async def test_mul_ele_methods(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/books")
    add_buttons_locator = async_page.locator("//input[@value='Add to cart']")
    add_buttons = await add_buttons_locator.all()
    for button in add_buttons:
        await button.click()
    async_page.wait_for_timeout(2000)


@pytest.mark.asyncio
async def test_mul_ele_methods(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/books")
    add_buttons_locator = async_page.locator("//input[@value='Add to cart']")
    print(await add_buttons_locator.count())
    add_buttons = await add_buttons_locator.all()
    for button in add_buttons:
        await button.click()
        await async_page.wait_for_timeout(2000)


#books = ["Computing and Internet","Fiction","Health Book"]
@pytest.mark.asyncio
async def test_mul_ele_methods(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/books")
    # books = ["Computing and Internet", "Fiction", "Health Book"]
    books_name = "Fiction"
    book = async_page.locator(f"//a[text()='{books_name}']/../..//input[@value='Add to cart']")
    await book.click()
    await async_page.wait_for_timeout(2000)
    books = ["Computing and Internet", "Fiction", "Health Book"]
    for i in books:
        book = async_page.locator(f"//a[text()='{i}']/../..//input[@value='Add to cart']")
        await book.click()
        await async_page.wait_for_timeout(2000)

@pytest.mark.asyncio
async def test_mul_ele_methods(async_page):
    await async_page.goto("https://demowebshop.trice")
