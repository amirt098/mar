from playwright.sync_api import sync_playwright
import time

def twitter_crawler(username):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(f"https://twitter.com/{username}")
        time.sleep(3)

        tweets = page.locator("article div[lang]").all_text_contents()
        for tweet in tweets[:5]:
            print(tweet)

        browser.close()

twitter_crawler("elonmusk")
