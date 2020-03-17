from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:

    def __init__(self, username, pwd):
       self.username = username
       self.pwd = pwd
       self.bot = webdriver.Chrome("Drivers/chromedriver.dmg")

    def login(self):
        bot = self.bot
        bot.get("https://twitter.com")
        time.sleep(3)
        email = bot.find_element_by_class_name("email-input")
        password = bot.find_element_by_name("session[password]")
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.pwd)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_tweets(Self, hashtag):
        bot = self.bot
        bot.get("https://twitter.com/search?q=" + hashtag + "&src=typed_query")
        time.sleep(3)
        for i in range(0, 3):
            bot.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(2)
            tweets = bot.find_elements_by_class_name("tweet")
            links = [elem.get_attribute("data-permalink-path") for elem in tweets]
            print(links)
            for link in links:
                bot.get("https://twitter.com" + link)
                try:
                    bot.find_element_by_class_name("HeartAnimation").click()
                    time.sleep(5)
                except Exception as e:
                    print("Exception ", e)

user_account = TwitterBot("8130327281", "Komal@1997")
user_account.login()
user_account.like_tweets("webdevelopment")