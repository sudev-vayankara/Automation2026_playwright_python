import pytest
from playwright.async_api import async_playwright
from pytest_check import check
from pathlib import Path

# @pytest.mark.asyncio
# async def test_playwright():
#     async with async_playwright() as p:
#        browser = await p.chromium.launch(headless=False)
#        page = await browser.new_page()
#        await page.goto("https://demowebshop.tricentis.com/")
#        title = await page.title()
#        #assert title
#        check.is_true(
#            bool(title.strip()) , "title is missing"
#        )
#         # img is alt
#        missingalt = await page.locator("img:not([alt])").count()
#        check.equal(missingalt, 0, f"{missingalt} img missing with alt")

#        main_count =await page.locator("main").count()
#        check.is_true(main_count>=1, f"main count is 0")


# @pytest.mark.asyncio
# async def test_playwright():
#     async with async_playwright() as p:
#        browser = await p.chromium.launch(headless=False)
#        page = await browser.new_page()
#        await page.goto("https://demowebshop.tricentis.com/")
#        title = await page.title()
#        #assert title
#        check.is_true(
#            bool(title.strip()) , "title is missing"
#        )
#         # img is alt
#        missingalt = await page.locator("img:not([alt])").count()
#        check.equal(missingalt, 0, f"{missingalt} img missing with alt")

#        main_count =await page.locator("main").count()
#        check.is_true(main_count>=1, f"main count is 0")

#        # Load axe-core JavaScript
#        axe_path = Path("node_modules/axe-core/axe.min.js")
#        check.is_true(axe_path.exists(), "Install axe-core using npm")
#        if not axe_path.exists():
#          return

#        await page.add_script_tag(
#           path = str(axe_path)
#        )

#        resu = await page.evaluate(
#         " ""
#         async () => {
#         return await axe.run(document);
#         }
#         " ""
#        )

# v = resu["violations"]
#        v = resu["violations"]
#        for i in v:
#           print(f"Rule : {v['id']}")
#           print(f"Impact :{v['impact']}" )
#           print(f"Description: {v['description']}")
#           for node in i:
#              print("Affected element:", node["target"])
#              print("Details:", node["failureSummary"])
#        check.equal(
#           len(v) , 0 , f" accessability  : {len(v)}" 
#        )
#        await browser.close()



# @pytest.mark.asyncio
# async def test_playwright():
#     async with async_playwright() as p:
#        browser = await p.chromium.launch(headless=False)
#        page = await browser.new_page()
#        await page.goto("https://demowebshop.tricentis.com/")
#        await page.wait_for_timeout(5000)
#        await page.screenshot(path = "screenshots/page.png")
#        await page.screenshot(path = "screenshots/full_page.png",full_page=True)
#        await page.locator("#twotabsearchtextbox").screenshot(path = "screenshots/ele.png")


# @pytest.mark.asyncio
# async def test_playwright():
#     async with async_playwright() as p:
#        browser = await p.chromium.launch(headless=False)
#        page = await browser.new_page()
#        await page.goto("https://demowebshop.tricentis.com/")
#        await page.screenshot(
#           path =  "screenshots/ele_page.png",
#           full_page=True,
#           mask = [
#              page.locator("//input[@value='Add to cart']"),
#              page.locator("#small-searchterms")
#           ],
#           mask_color="red" # "#FF00FF"

#        )



from PIL import Image




@pytest.mark.asyncio
async def test_playwright():

    # Create screenshots folder
    path = Path(r"C:\Users\User\Documents\screenshots")
    path.mkdir(parents=True, exist_ok=True)

    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # Set viewport size
        await page.set_viewport_size({
            "width": 1280,
            "height": 800
        })

        # Open website
        await page.goto("https://demowebshop.tricentis.com/")

        # Take logo screenshot
        await page.locator(".header-logo").screenshot(
            path=str(path / "logo.png")
        )

        # Take full-page screenshot
        await page.screenshot(
            path=str(path / "full_page.png"),
            full_page=True
        )

        # Open the full-page screenshot using Pillow
        with Image.open(path / "full_page.png") as img:

            # Get image dimensions
            w, h = img.size

            print("Image width:", w)
            print("Image height:", h)

            # Crop the top 250 pixels
            crop_ = (0, 0, w, 250)

            cro_img = img.crop(crop_)

            # Resize the cropped image
            tag_size = (800, 150)

            re_size_img = cro_img.resize(
                tag_size,
                Image.Resampling.LANCZOS
            )

            # Save resized image
            re_size_img.save(path / "re_size.png")

        await browser.close()