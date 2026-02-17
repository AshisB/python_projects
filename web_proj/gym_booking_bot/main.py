ACCOUNT_EMAIL = "nujayabia@gmail.com"  # The email you registered with
ACCOUNT_PASSWORD = "Nuj@y@123!@#"      # The password you used during registration
GYM_URL = "https://appbrewery.github.io/gym/"




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os




user_data_dir=os.path.join(os.getcwd(),"chrome_profile")
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
# Add stability arguments to prevent the crash
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-setuid-sandbox")
chrome_options.add_argument("--disable-extensions")

# Optional: Specify profile directory explicitly
chrome_options.add_argument(f"--profile-directory=Default")

browser=webdriver.Chrome(options=chrome_options)
browser.get(GYM_URL)
browser.maximize_window


wait=WebDriverWait(browser,10)

#clicking login button
login_button=wait.until(EC.element_to_be_clickable((By.ID,'login-button')))
login_button.click()
try:
    #email field
    email=wait.until(EC.visibility_of_element_located((By.NAME,"email")))
    email.clear()
    email.send_keys(ACCOUNT_EMAIL,Keys.TAB)
    #password field
    password=wait.until(EC.visibility_of_element_located((By.NAME,"password")))
    password.clear()
    password.send_keys(ACCOUNT_PASSWORD,Keys.TAB,Keys.ENTER)

    # Wait for schedule page to load
    wait.until(EC.presence_of_element_located((By.ID, "schedule-page")))

except TimeoutException:
    print("Sorry Timeout")    
    browser.save_screenshot('form-error.png')
    raise