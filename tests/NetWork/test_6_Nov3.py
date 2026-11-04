import pytest
from pytest_check import check
from playwright.async_api import async_playwright






@pytest.mark.asyncio
async def test_playwright():
    async with async_playwright() as p:
       browser = await p.chromium.launch(headless=False)
       page = await browser.new_page()
       await page.goto("https://www.amazon.in/")
       title = await page.title()
       #assert title
       check.is_true(
           bool(title.strip()) , "title is missing"
       )
        # img is alt
       missingalt = await page.locator("img:not([alt])").count()
       check.equal(missingalt, 0, f"{missingalt} img missing with alt")

       main_count =await page.locator("main").count()
       check.is_true(main_count>=1, f"main count is 0")

       # Load axe-core JavaScript
       axe_path = Path("node_modules/axe-core/axe.main.js")
       check.is_true(axe_path.exists(), "Install axe-core using npm")
       if not axe_path.exists():
         return

       await page.add_script_tag(
          path = str(axe_path)
       )

       resu = await page.evaluate(
          """
          async ()=>{
           await axe.run(document);
          }
          """
       )
       v = resu["violations"]
       for i in v:
          print(f"Rule : {v['id']}")
          print(f"Impact :{v['impact']}" )
          print(f"Description: {v['description']}")
          for node in i:
             print("Affected element:", node["target"])
             print("Details:", node["failureSummary"])
       check.equal(
          len(v) , 0 , f" accessability  : {len(v)}" 
       )
       await browser.close()


#capturing screenshot

@pytest.mark.asyncio
async def test_playwright():
    async with async_playwright() as p:
       browser = await p.chromium.launch(headless=False)
       page = await browser.new_page()
       await page.goto("https://www.amazon.in/")
       await page.wait_for_timeout(5000)
       await page.screenshot(path = "screenshots/page.png")
       await page.screenshot(path = "screenshots/full_page.png",full_page=True)
       await page.locator("#twotabsearchtextbox").screenshot(path = "screenshots/ele.png")