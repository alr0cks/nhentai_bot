#!/usr/bin/env python

from telegraph import Telegraph
import scrape
import requests
from bs4 import BeautifulSoup
import re
import json


url = "https://nhentai.net/g/39471/"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

content_page = scrape.get_info(soup,url)

title1 = soup.find('h1').text   #title
title2 = soup.find('h2').text   #title in japnese
article = soup.find("h3",{"id":"gallery_id"}).text      #hash id

telegraph = Telegraph()

telegraph.create_account(short_name='1337')

response = telegraph.create_page(
    str(title1),
    html_content = f"""
  <p>{content_page}</p>
    """
)

print('https://telegra.ph/{}'.format(response['path']))
