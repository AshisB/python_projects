ACCOUNT_EMAIL = "nujayabia@gmail.com"  # The email you registered with
ACCOUNT_PASSWORD = "Nuj@y@123!@#"      # The password you used during registration
GYM_URL = "https://appbrewery.github.io/gym/"


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException
import os
from datetime import datetime, timedelta

booked_count=0
waitist_count=0
already_booked_count=0


def get_next_day_time(day, time):
    """
    day: "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    time: "6:00 PM" or "18:00" or "9:00 AM" etc.
    """
    # Convert day name to number (Monday=0, Sunday=6)
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    day_num = days.index(day.lower())
    
    # Parse time
    time = time.lower().replace(" ", "")
    if "am" in time or "pm" in time:
        hour = int(time.split(":")[0])
        minute = int(time.split(":")[1][:2]) if ":" in time else 0
        if "pm" in time and hour != 12:
            hour += 12
        if "am" in time and hour == 12:
            hour = 0
    else:
        hour, minute = map(int, time.split(":"))
    
    # Calculate next occurrence
    today = datetime.now()
    days_ahead = (day_num - today.weekday()) % 7
    if days_ahead == 0:
        days_ahead = 7
    
    next_date = today + timedelta(days=days_ahead)
    next_datetime = next_date.replace(hour=hour, minute=minute, second=0, microsecond=0)
    
    return next_datetime.strftime("%Y-%m-%d-%H%M")

# **************************user interaction for booking**********************

print("\nPlease make your booking.Time and date")

user_day_raw=input("Enter your days eg. sunday,monday: ").lower()
user_day_list=user_day_raw.split(",")

time=input("Enter your time: ").lower()
print(user_day_list)

#********************selenium webdriver launching ***************************

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

#**********************clicking login button logic**************************

login_logout_button=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.Navigation_rightSection__L2XbA button')))
if login_logout_button.get_attribute("innerText")=="Login":
    login_logout_button.click()
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
else:
    class_schedule=wait.until(EC.element_to_be_clickable((By.ID,"schedule-link")))    
    class_schedule.click()        
print('hello out of try except for login button')


#**********************finding user requested day and find booking button**************************

try:
    day_list=wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME,"Schedule_dayGroup__y79__")))
    print(len(day_list))
    for day in day_list:
        day_string=day.get_attribute("id")
        for user_day in user_day_list:
            user_day_str=user_day[:3]
            date_time_str=get_next_day_time(user_day, time)
            print(date_time_str)
            if user_day_str in day_string:
                date_booking_text = day.find_element(By.CSS_SELECTOR, ".Schedule_dayTitle__YBybs").text
                booking_class_name=day.find_element(By.XPATH,"descendant::h3").text
                book_button = day.find_element(By.CSS_SELECTOR, f"button[id$='{date_time_str}']")
                print(book_button)
                button_text=book_button.text


            #**********************Checking bookings and taking actions************************   

                if button_text =="Booked":
                    already_booked_count+=1
                    print(f"✓ Already booked: {booking_class_name} on {date_booking_text}")
                elif button_text=="Waitlisted":
                    already_booked_count+=1
                    print(f"✓ Already on waitlist: {booking_class_name} on {date_booking_text}")
                elif button_text=="Book Class":  
                    book_button.click()
                    booked_count+=1
                    print(f"Succesfully booked Thank you 😁")
                elif button_text=="Join Waitlist":  
                    book_button.click()
                    waitist_count+=1
                    print(f"Succesfully added to waitlist Thank you 😁")

#**********************Checking bookings and taking actions end************************   
except TimeoutException:    
    print("Sorry Timeout")    
    browser.save_screenshot('form-error.png')
except NoSuchElementException:
    print("Sorry Requested not found")    