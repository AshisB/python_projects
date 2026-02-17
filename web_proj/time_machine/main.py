from bs4 import BeautifulSoup
import requests
print('Welcome! to Time Machine fren')
year=input('Enter a year you want to vist in YYYY-MM-DD format: ')

URL=f"https://www.billboard.com/charts/hot-100/{year}/"

browser_headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
}

response=requests.get(url=URL,headers=browser_headers)
print(response.text)