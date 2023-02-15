import requests
from pathlib import Path,os
from dotenv import load_dotenv
load_dotenv()

# Autenticação da API escamoteando a senha com dotenv
news_api_key = str(os.getenv('news_api_key'))
url = f"http://newsapi.org/v2/top-headlines?country=br&apikey={news_api_key}"
main_page =requests.get(url).json()
article = main_page["articles"]

author = []
title = []
description = []

for ar in article:
    author.append(ar["author"])
    title.append(ar["title"])
    description.append(ar["description"])
for i in range(6):
    print(f"{i + 1} {author[i]} - {title[i]} - {description[i]}  \n") 
 

