from bs4 import BeautifulSoup
import requests

# with open('website.html','r') as f:
#     contents=f.read()
# # print(contents)     

# soup=BeautifulSoup(contents,"html.parser")
# print(soup.title.string)

response=requests.get(url="https://news.ycombinator.com/news")
response.raise_for_status
html_response=response.text

soup=BeautifulSoup(html_response,"html.parser")
site_data = soup.select('.titleline > a:first-child')
site_names=[site.string for site in site_data]
site_links=[site.get('href') for site in site_data]
site_vote_counts=[data.string.split(" ")[0] for data in soup.select('.subline .score')]
print(site_names)
print(site_links)
print(site_vote_counts)

max_value=max(site_vote_counts)
index=site_vote_counts.index(max_value)
print(f'{max_value},{index}')
print(f"Max value site name is {site_names[index]} and link is {site_links[index]}")

