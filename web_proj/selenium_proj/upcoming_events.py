from selenium import webdriver
from selenium.webdriver.common.by import By


browser=webdriver.Chrome()
browser.get("https://www.python.org/")
date_data=browser.find_elements(By.CSS_SELECTOR,value=".event-widget time")

date_list=[date.get_attribute("datetime").split("T")[0] for date in date_data]
print(date_list)
event_list=[]
for count in range(1,len(date_list)+1):
    event_data=browser.find_element(By.XPATH,value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{count}]/a')
    event_list.append(event_data.text)
print(event_list)

final_dict={index:{"time":date,"event":event} for index,date in enumerate(date_list) for event in event_list}


print(final_dict)