import pytest
from playwright.async_api import async_playwright

@pytest.mark.asyncio
async def test_perfomnce():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            record_har_path="network_traffic.har"
        )
        page = await context.new_page()

        async def log_res(response):
            req = response.request
            timing = req.timing

            start = timing.get("startTime",0)
            end = timing.get("endTime",-1)
            if(end >= 0):
                duration = end - start
                print(
                    f"status : {req.status} "
                    f"Time :{duration:.2f }ms"
                    f"url : {req.url}"
                )

        page.on("response", lambda response: asyncio.create_task(log_res(response)))

        await page.goto("https://demowebshop.tricentis.com/")
        await page.get_by_text("Register").click()
        await page.wait_for_timeout(1000)
        await context.close()
        await browser.close()


#   1. Measuring page performance metrics
@pytest.mark.asyncio
async def test_perfomnce_metrics():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page =await browser.new_page()
        resp = await page.goto("https://demowebshop.tricentis.com/")
        assert resp is not None
        assert resp.status < 400

        metrics = await page.evaluate(
            """()=>{
          const timings =  performance.getEntriesByType(
            'navigation')[0];
                return {
                    domContentLoaded: timings.domContentLoadedEventEnd - timings.startTime,
                    loadEvent: timings.loadEventEnd - timings.startTime,
                    resp_time: timings.responseEnd - timings.requestStart,
                    resoucesCount: performance.getEntriesByType('resource').length
                };
        }"""
        )
        print("HTTP status code :" ,resp.status )
        print("performance metrix : " ,metrics)
        await browser.close()



@pytest.mark.asyncio
async def test_trace_localhost():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        await context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )

        try:
            page = await context.new_page()
            await page.goto("http://localhost:3000/")
            print("Page title:", await page.title())

            await page.wait_for_load_state("networkidle")

        finally:
            await context.tracing.stop(path="trace.zip")
            await browser.close()




#Tracing performance with Trace Viewer
@pytest.mark.asyncio
async def test_trace_localhost():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        await context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )

        try:
            page = await context.new_page()
            await page.goto("http://localhost:3000/")
            print("Page title:", await page.title())

            await page.wait_for_load_state("networkidle")

        finally:
            await context.tracing.stop(path="trace.zip")
            await browser.close()

#Generating Lighthouse scores via Playwright integration
# (0 to 100)
# node:-->
#npm install --save-dev lighthouse

@pytest.mark.asyncio
async def test_lighthouse_audit():
    url = "https://demowebshop.tricentis.com/"
    async with async_playwright() as p :
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(url)
        await page.wait_for_timeout(1000)
        await browser.close()

    project_dir = Path(__file__).resolve().parent
    report_path = project_dir / "light_house.json"

    result = subprocess.run(
        [
            "npx.cmd",
            "lighthouse",
            url,
            "--chrome-flags=--headless",
            "--output=json",
            f"--output path = {report_path}"
        ],
        cwd= str(project_dir),
        capture_output = True,
        text=True,
        timeout=180,
        shell=False
       )
    if result.returncode != 0:
        print(f"Lighthouse is failed  studout : {result.stdout}  , error : {result.stderr} ")

    with open(report_path,encoding="utf-8") as file:
        json_data = json.load(file)
        for name in ("performance", "accessibility", "best-practices", "seo"):
            score = json_data["categories"][name]["score"]
            print(f"{name} : {score * 100:.0f}/100")