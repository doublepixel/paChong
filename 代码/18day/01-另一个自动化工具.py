# -*- coding:utf-8 -*-
import asyncio
from pyppeteer import launch


async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('http://www.baidu.com/')
    await asyncio.sleep(100)
    await browser.close()



asyncio.get_event_loop().run_until_complete(main())
