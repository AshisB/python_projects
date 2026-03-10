"""
Title:       "Zillow Scraping and Automation Bot"
Description: This program helps us to scrape rent data from Zillow clone site
             and then populate to spreadsheet using bot.
"""

#********************************packages used and versions*****************************************
"""
Dependencies
________________
beautifulsoup4        4.14.3
selenium             4.41.0
fuzzywuzzy           0.18.0
python-Levenshtein   0.27.3

Python version: 3.13.1

Author: [Ashis B. Maharjan]
Date: March 2026

"""

#********************************Program Start*****************************************

from bs4 import BeautifulSoup
# import undetected_chromedriver as uc
from selenium import webdriver
from scraping_data import Scraping
from automating import AutomateBot
import os
from helpers import *



if __name__=="__main__":
    user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--lang=en-US')# for force english language for sites
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    # These 3 lines below help Chrome run smoothly and facilitate  your saved login session
    # They prevent crashes by fixing common permission and memory issues

    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resources
    chrome_options.add_argument("--remote-debugging-port=9222")  # Explicitly set debug port

    browser = webdriver.Chrome(options=chrome_options)
    retry_logic(browser.get(url="https://appbrewery.github.io/Zillow-Clone/"))
    random_sleep(5)

    #**************************************Scraping model******************************
    html_response=browser.page_source
    soup=BeautifulSoup(html_response,'html.parser')
    scraping_obj=Scraping(soup)
    prices=scraping_obj.price
    address=scraping_obj.address
    links=scraping_obj.link

    #********************************Automation google form started**********************
    automate_obj=AutomateBot(prices,address,links,browser)

    print('Successfully completed task. Thank you!!')


#********************************Program End*****************************************