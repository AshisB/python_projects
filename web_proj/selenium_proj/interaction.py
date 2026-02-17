from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
browser=webdriver.Chrome(options=chrome_options)

# browser.get("https://en.wikipedia.org/wiki/Main_Page")

# articles_count=browser.find_element(By.CSS_SELECTOR,value="#articlecount ul li a")
# articles_count.click()
# print(articles_count.text)



browser.get("https://secure-retreat-92358.herokuapp.com/")
fname=browser.find_element(By.NAME,value="fName")
fname.clear()
fname.send_keys("AshisB",Keys.TAB)

lname=browser.find_element(By.NAME,value="lName")
lname.clear()
lname.send_keys("Maharjan",Keys.TAB)

email=browser.find_element(By.NAME,value="email")
email.clear()
email.send_keys("maharjanashis@gmail.com",Keys.ENTER)

