# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("https://twitter.com/elonmusk")
#
# tweets = driver.find_elements("//article[@role='article']")
# for tweet in tweets:
#     print(tweet.text)
#
# driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


# Function to scrape tweets
def scrape_tweets(username):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(f'https://twitter.com/{username}')
        time.sleep(5)

        tweets = driver.find_elements(By.XPATH, '//article[@data-testid="tweet"]')

        # Extract tweet information
        for tweet in tweets:
            print(tweet)
            tweet_id = tweet.get_attribute('data-tweet-id')
            # likes = tweet.find_element(By.XPATH, './/div[@data-testid="like"]').text
            # retweets = tweet.find_element(By.XPATH, './/div[@data-testid="retweet"]').text

            print(f'Tweet ID: {tweet_id}, Likes: {"likes"}, Retweets: {"retweets"}')

    finally:
        driver.quit()


scrape_tweets('elonmusk')