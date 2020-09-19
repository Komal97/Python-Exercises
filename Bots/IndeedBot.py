from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

class IndeedBot:
    
    def __init__(self):
    #    self.username = username
    #    self.pwd = pwd
       self.driver = webdriver.Chrome("Drivers/chromedriver.dmg")
       self.query_string = "https://www.indeed.com/jobs?q={job}&l={city}%2C+{state}"
       self.jobs = []
       self.express_apply_jobs = []

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

user_account = IndeedBot("USER_ID", "PASSWORD")
user_account.login()
