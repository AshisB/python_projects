UPLOAD_SPEED=20
DOWNLOAD_SPEED=50


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from speedtesttwitterbot import SpeedtestTwitterbot
from twitter import Twitter
import os
import time
from dotenv import load_dotenv

load_dotenv()
twitter_username=os.getenv("TWITTER_USERNAME")
twitter_password=os.getenv("TWITTER_PASSWORD")


user_data_dir=os.path.join(os.getcwd(),"chrome_profile")
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_argument("--no-sandbox")  # 👈 CRITICAL
chrome_options.add_argument("--disable-dev-shm-usage")  # 👈 CRITICAL
chrome_options.add_argument("--remote-debugging-port=9222")  # 👈 CRITICAL for Chrome 136+

browser=webdriver.Chrome(options=chrome_options)#browser set
wait=WebDriverWait(browser,10)#wait set
speedtest_twitterbot_obj=SpeedtestTwitterbot(browser,wait,twitter_username,twitter_password)

def maximize_speedtest_window(site_url):
    browser.get(site_url)
    browser.maximize_window()

    
if __name__=="__main__":
    print('Twitter for tweeting and tagging ISP for slow network.')#started program
#***************************Speed test site started***************************************
    maximize_speedtest_window("https://www.speedtest.net/")
 
    go_clicked=speedtest_twitterbot_obj.retry_logic(speedtest_twitterbot_obj.click_go)
    if(go_clicked):
        speed_isp=speedtest_twitterbot_obj.retry_logic(speedtest_twitterbot_obj.check_bandwidth)
        print(speed_isp)
        for i in range(1,speedtest_twitterbot_obj.retries+1):
            if speed_isp['download']=='' or speed_isp['download']=='—' or speed_isp['upload']=='—':
                print('Waitng for values:')
                print(f"value check {i}")
                speed_isp=speedtest_twitterbot_obj.retry_logic(speedtest_twitterbot_obj.check_bandwidth)
                time.sleep(2**i)
            else:
                print(speed_isp)
                break    
        

#***************************Twitter  site started***************************************

        if float(speed_isp['download'])<float(DOWNLOAD_SPEED):#condition checked
            maximize_speedtest_window("https://x.com/i/flow/login")
            print('Succesfully opened twitter.')
            print(browser.window_handles)
            print(len(browser.window_handles))
            time.sleep(8)
            success_login=speedtest_twitterbot_obj.retry_logic(speedtest_twitterbot_obj.login_twitter)
            print(success_login)
        else:
            print("Speed found as committed.")    






