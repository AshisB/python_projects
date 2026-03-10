from selenium.common.exceptions import TimeoutException,NoSuchElementException
import time
import random

def retry_logic(func, retries=7):
        for count in range(1,retries+1):
            try:
                print(f"check {count}")
                return func
            except TimeoutException:
                print(f'There was some error. Time out!!')
            except NoSuchElementException as e:
                print(f'There was some error {e}.')
            except Exception as e:
                print(f'There was some error {e}.')
        return None

def random_sleep(seco):
    random_time=random.randint(seco,seco+4)
    print(f"wait {random_time}")
    time.sleep(random_time)
