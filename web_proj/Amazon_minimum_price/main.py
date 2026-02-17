import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
import os
import re


load_dotenv()

URL="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
set_price=100


site_headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
    "Accept-Encoding": "gzip, deflate, br, zstd", 
    "Accept-Language": "en-US,en;q=0.9", 
    "Priority": "u=0, i", 
    "Sec-Ch-Ua": "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Google Chrome\";v=\"144\"", 
    "Sec-Ch-Ua-Mobile": "?0", 
    "Sec-Ch-Ua-Platform": "\"Windows\"", 
}


# Making request to site
response=requests.get(url=URL,headers=site_headers)
html_response=response.text




# Making soup from site html
soup=BeautifulSoup(html_response,"html.parser")
all_prices = []
for script in soup.find_all('script'):
    if script.string:
        prices = re.findall(r'\$\d+(?:\.\d{2})?', script.string)
        all_prices.extend(prices)

print(f"All prices found: {list(all_prices)}")
# This might show both $59.71 and $69.98
# print(soup.prettify())
# price=soup.select_one('.aok-offscreen').string
# item_name=soup.select_one('#productTitle').string
# price_box = soup.select_one(".olpWrapper.a-size-small")
# print(price_box)
item_name=soup.select_one('#productTitle').string
price=all_prices[0]
print(price)

price_number=float(price.replace("$",""))
print(price_number)
item_name_short=item_name.split(",")[0]
item_name_short=" ".join(item_name_short.split())
print(item_name_short)


sender_email =os.getenv('SENDER_EMAIL')
receiver_email=os.getenv('REVEIVER_EMAIL')
sender_password =os.getenv('APP_PASSWORD')

print(f"{sender_email},{receiver_email},{sender_password}")
message=f'Subject:Price Alert:\n\n price alert less than your set price.\n You can now get {item_name_short} in {price}'
if(price_number<set_price):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=sender_email,password=sender_password)
        connection.sendmail(sender_email,receiver_email,message)
        print('mail sent succesfully.')
     