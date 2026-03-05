import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from twitter import Twitter
import os
import time
import random
from selenium.webdriver.support.ui import WebDriverWait
from speedtesttwitterbot import SpeedtestTwitterbot

from dotenv import load_dotenv

UPLOAD_SPEED=20
DOWNLOAD_SPEED=50




load_dotenv()
twitter_username=os.getenv("TWITTER_USERNAME")
twitter_password=os.getenv("TWITTER_PASSWORD")


user_data_dir=os.path.join(os.getcwd(),"chrome_profile")
chrome_options=uc.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
chrome_options.add_argument("--profile-directory=Default")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

# chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# chrome_options.add_experimental_option("useAutomationExtension", False)


browser=uc.Chrome(options=chrome_options,version_main=145)#browser set
wait=WebDriverWait(browser,10)#wait set
speedtest_twitterbot_obj=SpeedtestTwitterbot(browser,wait,twitter_username,twitter_password)

def maximize_site_window(site_url):
    browser.get(site_url)
    browser.maximize_window()

    
if __name__=="__main__":
    print('Twitter for tweeting and tagging ISP for slow network.')#started program
#***************************Speed test site started***************************************
    # maximize_site_window("https://www.speedtest.net/")
 
    # go_clicked=speedtest_twitterbot_obj.retry_logic(speedtest_twitterbot_obj.click_go)
    # if(go_clicked):
    if len(twitter_username)>0:
    #     speed_isp=speedtest_twitterbot_obj.retry_logic(speedtest_twitterbot_obj.check_bandwidth)
    #     print(speed_isp)
    #     for i in range(1,speedtest_twitterbot_obj.retries+1):
    #         if speed_isp['download']=='' or speed_isp['download']=='—' or speed_isp['upload']=='—':
    #             print('Waitng for values:')
    #             print(f"value check {i}")
    #             speed_isp=speedtest_twitterbot_obj.retry_logic(speedtest_twitterbot_obj.check_bandwidth)
    #             time.sleep(2**i)
    #         else:
    #             print(speed_isp)
    #             break    
        

#***************************Twitter  site started***************************************

        # if float(speed_isp['download'])<float(DOWNLOAD_SPEED):#condition checked
        if len(twitter_username)>0:
            
            for _ in range(5):   
                time.sleep(random.randint(2,4)) 
                try:
                    maximize_site_window("https://x.com/i/flow/login")
                    print('Succesfully opened twitter.')
                    print(browser.window_handles)
                    print(len(browser.window_handles))
                    time.sleep(random.randint(4,7)) 
                    success_login=speedtest_twitterbot_obj.retry_logic(speedtest_twitterbot_obj.login_twitter)
                    print(success_login)
                    break
                except:
                    print("Site not reachable or cannot maximize becaise of some problem.")        
        else:
            print("Speed found as committed.")    
print("🎉 All tasks completed!")
print("🔵 Browser will stay open. Close it manually when done.")
input("Press Enter to exit this script (browser will close)...")





