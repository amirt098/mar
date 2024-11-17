from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()


def fetch_tweets(query, num_scrolls=5):
    url = f'https://twitter.com/elonmusk'
    driver.get(url)
    time.sleep(2)

    tweet_list = []
    for _ in range(num_scrolls):
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        tweets = soup.find_all('div', {'data-testid': 'tweet'})

        for tweet in tweets:
            try:
                text = tweet.find('div', {'lang': True}).text
                tweet_list.append(text)
            except:
                continue

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

    driver.quit()
    return tweet_list


tweets = fetch_tweets("Trump", 3)
for tweet in tweets:
    print(tweet)
