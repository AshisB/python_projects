from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from helpers import *


class AutomateBot:
    def __init__(self,prices,address,links,browser):
        self.prices=prices
        self.address=address
        self.links=links
        self.browser=browser
        self.get_google_form()


    def customize_wait(self,element,time=10):
        return WebDriverWait(element,time)

    def get_google_form(self):
        print('Google form Opening...')
        self.browser.execute_script("window.open('');")
        self.browser.switch_to.window(self.browser.window_handles[1])
        retry_logic(self.browser.get(url="https://forms.gle/Yw6FXpUQZBXkgP8b6"))
        self.automate_all_data()

    def automate_all_data(self):
        global index
        for index in range(len(self.prices)):
            res=retry_logic(self.enter_form_data(index))
            if res:
                print(f"Property number {index+1} entered")


    def enter_form_data(self,i):
        random_sleep(4)
        print(f"Starting entering property {i+1}")
        #*****************form filling**********************
        wait=self.customize_wait(self.browser,10)
        all_fields=wait.until(EC.presence_of_all_elements_located((By.XPATH,'//input[@jsname="YPqjbf"]')))

        address=all_fields[0]
        price=all_fields[1]
        link=all_fields[2]

        address.clear()
        address.send_keys(self.address[i],Keys.TAB)

        price.clear()
        price.send_keys(self.prices[i], Keys.TAB)

        link.clear()
        link.send_keys(self.links[i], Keys.TAB)

        submit_btn=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')))
        submit_btn.click()

        random_sleep(4)

        resubmit_btn=wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')))
        resubmit_btn.click()

        return True

