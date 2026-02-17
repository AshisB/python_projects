from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_option=webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach',True)


browser=webdriver.Chrome(options=chrome_option)
browser.get(url='https://www.daraz.com.np/products/stainless-steel-cordless-electric-jug-18-ltr-1500-watts-i502504267-s2250144682.html?pvid=c9d380b0-7a16-4044-ac89-341cfcab83f3&search=jfy&scm=1007.51705.481011.0&spm=a2a0e.tm80335409.just4u.d_502504267')
browser.maximize_window()


price_css_selector=browser.find_element(By.CSS_SELECTOR,value=".pdp-product-price span")
print(price_css_selector.text)

button=browser.find_element(By.CLASS_NAME,value="im-app__minimize-title")
print(button.text)


search_box=browser.find_element(By.NAME,value='q')
print(search_box.get_attribute('placeholder'))
search_box.click()
search_box.clear()
search_box.send_keys("hot pot")

search_button=browser.find_element(By.XPATH,value='//*[@id="topActionHeader"]/div[1]/div[2]/div/div[2]/div/form/div/div[2]/a')
search_button.click()

# browser.quit()