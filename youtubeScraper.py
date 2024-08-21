import asyncio
import os
import json
import sys
import select
from dotenv import load_dotenv
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
from uuid import uuid4

load_dotenv()

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto('https://www.youtube.com/')
        try:
            content = await page.content()
            soup = BeautifulSoup(content, 'html.parser')
            print('Page loaded')
            #find the search bar
            searchBar = await soup.find('input',{'id': 'search'})
            if searchBar:
                await page.click('input["id=search"]')
                await searchBar.fill('carbonara')
                contentAfterSearch = await page.content()
                soupAfterSearch = BeautifulSoup(contentAfterSearch, 'html.parser')
                print('Search bar filled')


            print('Search bar loaded')
            await page.fill('input#search', 'python')
            print('Search bar filled')
            await page.click('button#search-icon-legacy')
            print('Search button clicked')
            #after that await for the search results to load
            videos = await page.wait_for_selector('ytd-search-pyv-renderer')
            #find 'yt-interaction' element with id 'interaction' inside the video
            #and click on it
            await videos[0].click('yt-interaction[id="interaction"]')
            #wait for the video to load
            await page.wait_for_selector('video')
            #save video url into a file named video_url.txt
            video_url = await page.url()
            with open('video_url.txt', 'w') as f:
                f.write(video_url)
                print('Video URL saved')
        except Exception as e:
            print('Page not loaded', e)
        finally:
            await browser.close()
asyncio.run(main())