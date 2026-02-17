from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
browser=webdriver.Chrome(options=chrome_options)
browser.get("https://ozh.github.io/cookieclicker/")
browser.maximize_window()

#escape english language if present
time.sleep(5)
try:
    lang=browser.find_element(By.XPATH,value='//*[@id="langSelect-EN"]')
    lang.click()
except:    
    time.sleep(10)

cookie_btn=browser.find_element(By.CSS_SELECTOR,value="#bigCookie")   

def game_is_on():
    cookie_time=time.time()

    while time.time()-cookie_time<5:
        cookie_btn.click()
    store_list=[]
    time.sleep(3)
    try:
        cookie_accept = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".cc_btn_accept_all"))
        )
        cookie_accept.click()
        print("✅ Cookie banner accepted")
        time.sleep(1)  # Wait for banner to disappear
    except:
        print("No cookie banner found or already accepted")

    for i in range(0,19):
        store=browser.find_element(By.CSS_SELECTOR,value=f"#product{i}")
        if "enabled" in store.get_attribute("class"):  # Will see the enabled class
            print(i)
            print(store)
            store_list.append(store)

    store_list[-1].click()

start_time=time.time()
while time.time()-start_time<30:
    game_is_on()
cps_element = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "cookiesPerSecond")))
      
    # Get the text and clean it
cps_text = cps_element.text    
browser.quit()
print(f'Rate of cookie per second is:{cps_text}')