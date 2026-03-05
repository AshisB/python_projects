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
verified_booking_count=0


# def get_next_day_time(day, time):
#     """
#     day: "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
#     time: "6:00 PM" or "18:00" or "9:00 AM" etc.
#     """
#     # Convert day name to number (Monday=0, Sunday=6)
#     days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
#     day_num = days.index(day.lower())
    
#     # Parse time
#     time = time.lower().replace(" ", "")
#     if "am" in time or "pm" in time:
#         hour = int(time.split(":")[0])
#         minute = int(time.split(":")[1][:2]) if ":" in time else 0
#         if "pm" in time and hour != 12:
#             hour += 12
#         if "am" in time and hour == 12:
#             hour = 0
#     else:
#         hour, minute = map(int, time.split(":"))
    
    # Calculate next occurrence
    # today = datetime.now()
    # days_ahead = (day_num - today.weekday()) % 7
    # if days_ahead == 0:
    #     days_ahead = 7
    
    # next_date = today + timedelta(days=days_ahead)
    # next_datetime = next_date.replace(hour=hour, minute=minute, second=0, microsecond=0)
    
    # return next_datetime.strftime("%Y-%m-%d-%H%M")

# **************************user interaction for booking**********************
today=datetime.now()
today_name=today.strftime("%A").lower()
print(today_name)  
week_days=["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


print("\nPlease make your booking.Time and date")
while True:
    user_day=input("Enter your Booking day name : ").lower()
    if user_day in week_days:
        break
        # if today_name!=user_day:  only works when date range is 1  so commented 
        #     break
        # else:
        #     print(f'Booking date should not be today.Today is {user_day.upper()}')
    else:
        print('Incorrect day name')        
user_time=input("Enter your time: ").lower()
userclean=user_time.replace(' ', '').replace(':', '').replace('.', '').lower()

user_day_str=user_day[:3]
# date_time_str=get_next_day_time(user_day, time)
# print(date_time_str)

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
        if user_day_str in day_string:
           date_booking_text = day.find_element(By.CSS_SELECTOR, ".Schedule_dayTitle__YBybs").text
           booking_class_name=day.find_element(By.XPATH,"descendant::h3").text
           booking_time_list=day.find_elements(By.CSS_SELECTOR, "id^=['class-time']")
           for booked_time in booking_time_list:
               booked_time_text=booked_time.text()
               webclean=booked_time.replace(' ', '').replace(':', '').replace('.', '').lower()
               if userclean==webclean:
                   actions_div =booked_time.find_element(By.XPATH,"ancestors::div[@class='ClassCard_cardContent__WGvPp']")
                   book_button = actions_div.find_element(By.CSS_SELECTOR, ".ClassCard_cardActions__tVZBm button")
                   print(book_button.text)
                   button_text=book_button.text
               else:
                   print('Booking not found on that time. Retry selecting next time')
               













           


            # THEN find the button inside that div
           
        #  book_button = day.find_element(By.CSS_SELECTOR, f"button[id$='{date_time_str}']")
        #    book_button = day.find_element(By.XPATH, ".//button[starts-with(@id, 'book-button-')]")
    


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
# except NoSuchElementException:
#     print("Sorry Requested not found")    
# except:
#     print('Error while booking. Please try again.')    


#*************************************verify bookings**********************************

try:
    booking_link=wait.until(EC.element_to_be_clickable((By.ID,'my-bookings-link')))
    booking_link.click()

    wait.until(EC.presence_of_element_located((By.ID,'my-bookings-page')))

    all_booked_list=wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,'[id^=booking-card-booking_]')))
    for booked_class in all_booked_list:
        if '6:00 PM' in booked_class.find_element(By.XPATH,'descendant::p').text:
            verified_booking_count+=1
    print(all_booked_list)
    print(verified_booking_count)
    print(booked_count)
    difference_booking=verified_booking_count-booked_count
    if difference_booking==0:
        print(f'Succesfully booked {verified_booking_count} class for 6:00PM')
    elif difference_booking>0:
        print('There is something wrong with booking count update')  
    elif difference_booking<0:
        print('Bookings are not made sucesfully.')    

except TimeoutException:    
    print("Sorry Timeout")    
    browser.save_screenshot('form-error.png')
except NoSuchElementException:
    print("Sorry Requested not found")    

