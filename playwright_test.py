import asyncio
from playwright.sync_api import sync_playwright

#
# def twitter_crawler(username):
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=True)
#         page = browser.new_page()
#
#         tweet_url = "https://twitter.com/dangerscarf/status/1638163206349651975"
#         page.goto(tweet_url)
#
#         page.wait_for_selector("[aria-label='Reply']")
#
#         tweet = page.locator('[data-testid="tweet"]').inner_html()
#
#         print("Tweet Content:")
#         print(tweet)
#
#         browser.close()
#
#
# twitter_crawler("elonmusk")
#

from playwright.sync_api import sync_playwright


# def twitter_crawler(username):
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=True)
#         page = browser.new_page()
#
#         user_url = f"https://twitter.com/{username}"
#         page.goto(user_url)
#
#         page.wait_for_selector("[data-testid='tweet']")
#
#         tweets = page.query_selector_all("[data-testid='tweet']")
#
#         for tweet in tweets:
#             tweet_content = tweet.query_selector('[data-testid="tweetText"]').inner_text() if tweet.query_selector(
#                 '[data-testid="tweetText"]') else "No content"
#             author_name = tweet.query_selector('[data-testid="User-Names"]').inner_text() if tweet.query_selector(
#                 '[data-testid="User-Names"]') else "Unknown"
#             timestamp = tweet.query_selector('time').get_attribute('datetime') if tweet.query_selector(
#                 'time') else "No timestamp"
#
#             print("Tweet Content:", tweet_content)
#             print("Author:", author_name)
#             print("Timestamp:", timestamp)
#             print("-" * 40)
#
#         browser.close()
#
#
# twitter_crawler("elonmusk")


from playwright.sync_api import sync_playwright

from playwright.sync_api import sync_playwright

def crawl_twitter_profile(username, tweet_limit=100):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        url = f"https://twitter.com/{username}"
        page.goto(url)

        page.wait_for_selector('article')

        all_tweets = []
        last_height = 0

        while len(all_tweets) < tweet_limit:
            # Extract tweets currently loaded
            tweets = page.locator('article').evaluate_all(
                """
                (articles) => articles.map(article => {
                    const tweetText = article.querySelector('div[lang]')?.innerText || null;
                    const time = article.querySelector('time')?.getAttribute('datetime') || null;
                    const tweetId = article.querySelector('a[href*="/status/"]')?.getAttribute('href')?.split('/').pop() || null;
                    const stats = article.querySelectorAll('div[data-testid]');
                    const likes = stats[2]?.innerText || '0';
                    const retweets = stats[1]?.innerText || '0';
                    const comments = stats[0]?.innerText || '0';
                    return {
                        tweetId,
                        tweetText,
                        time,
                        likes,
                        retweets,
                        comments
                    };
                }).filter(tweet => tweet.tweetId && tweet.tweetText)
                """
            )

            # Add new tweets to the total list
            for tweet in tweets:
                if tweet not in all_tweets:  # Avoid duplicates
                    all_tweets.append(tweet)

            # Break if we already have enough tweets
            if len(all_tweets) >= tweet_limit:
                break

            # Scroll down to load more tweets
            page.evaluate("window.scrollBy(0, window.innerHeight)")
            page.wait_for_timeout(2000)  # Adjust if needed

            # Detect end of scroll (optional: could handle infinite scrolling issues)
            new_height = page.evaluate("document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        browser.close()
        return all_tweets[:tweet_limit]  # Return only the required number of tweets

# Example usage
if __name__ == "__main__":
    username = "elonmusk"
    tweets = crawl_twitter_profile(username, tweet_limit=100)
    for tweet in tweets:
        print(tweet)
