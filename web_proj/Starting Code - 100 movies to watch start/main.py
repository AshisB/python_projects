import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response=requests.get(url=URL)
response.raise_for_status()
html_response=response.text


soup=BeautifulSoup(html_response,'html.parser')
flim_title_list=soup.select('.article-title-description__text .title')
all_movies=[flim.string for flim in flim_title_list]
all_movies.reverse()
print(all_movies)
all_movies_string="Top 100 Movies\n"
for movie in all_movies:
    all_movies_string+=f'{movie}\n'
with open('Top_100_movies.txt','w',encoding='utf-8') as f:
    f.write(all_movies_string)




