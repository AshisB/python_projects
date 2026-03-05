from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from twitter import Twitter
import os
import time
import pyautogui
import windmouse
import random
from helpers_func import Helpers

class SpeedtestTwitterbot:
    def __init__(self,browser,wait,username,password):
        self.browser=browser
        self.wait=wait
        self.username=username
        self.password=password
        self.retries=7
        self.bandwidth={}
        self.helpers=Helpers()
    
    
    def retry_logic(self,func):
        print('entry')
        for attempt in range(1,self.retries+1):
            print(f'This is attempt {attempt}')
            try:
                result=func()
                return result
            except TimeoutException:
                print('Time is out,waiting.....')
            except NoSuchElementException:
                print('Element doesnot exist>>>')
            except Exception as e:
                print('Sorry!!!There is some problem.')       
                if attempt<= self.retries:
                    print(f'Error=>{e}')
        time.sleep(2 ** attempt)          

    def click_go(self):
        go_button=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a')))
        print(go_button)
        go_button.click()
        return True

    def check_bandwidth(self):
        download_speed=self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')))
        upload_speed=self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')))
        self.bandwidth={'download':download_speed.text,'upload':upload_speed.text}
        print(self.bandwidth)
        return self.bandwidth

            
  #*******************************twitter methods started*********************
    def login_twitter(self):
        while True:
            try:
                print(pyautogui.position())
                print('hello')
                time.sleep(10)
                # username enter
                self.helpers.humanlike_move_click(652,434)
                self.helpers.random_typing(self.username)
                print('username done')
                
                #password enter
                # self.helpers.humanlike_move_click(663,647)
                # self.helpers.random_typing(self.username)
                # print('password done')

                # login button
                self.helpers.humanlike_move_click(674,510)
                break
            except:
                print('twitter problem in login ......*')

        
        

























































    # def login_twitter(self):
    #     time.sleep(3)
    #     username_field=self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')))
    #     username_field.send_keys(self.username,Keys.TAB,Keys.ENTER)
    #     time.sleep(8)
    #     password_field=self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,'password')))
    #     password_field.send_keys(self.password)

    #     login_btn=self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.css-175oi2r r-b9tw7p button')))
    #     login_btn.click()
    #     return "Login successful"
    # def login_twitter(self):
    #     # Use the most stable selector - by name attribute
    #     username_field = self.wait.until(
    #         EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="text"]'))
    #     )
    #     username_field.send_keys(self.username)
        
    #     # Find and click Next button
    #     next_button = self.wait.until(
    #         EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Next')]"))
    #     )
    #     time.sleep(3)
    #     next_button.click()
    #     time.sleep(5)
    #     # Wait for password field
    #     password_field = self.wait.until(
    #         EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="password"]'))
    #     )
    #     password_field.send_keys(self.password)
        
    #     # Click Log in button
    #     login_button = self.wait.until(
    #         EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Log in')]"))
    #     )
    #     time.sleep(3)
    #     login_button.click()