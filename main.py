import requests
from bs4 import BeautifulSoup
from telegraph import Telegraph

import scrape
from argparse import ArgumentParser

parser = ArgumentParser(description="Script to give you allow you to easily read doujins as telegraph articles")
parser.add_argument("-s", "--source", help="The digits of the doujin", type=int)
args = parser.parse_args()

if not args.source:
    print("Please provide source to scrape")
    exit(1)

url = f"https://nhentai.net/g/{args.source}/"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

(
    title,
    title_jap,
    article,
    parodies,
    characters,
    tags,
    artist,
    groups,
    languages,
    categories,
    image_tags,
) = scrape.get_info(soup)

telegraph = Telegraph()

telegraph.create_account(short_name='1337')

response = telegraph.create_page(str(title), html_content=image_tags,)

print('https://telegra.ph/{}'.format(response['path']))
print("title :", title)
print("title_jap :", title_jap)
print("article :", article)
print("parodies :", parodies)
print("characters :", characters)
print("tags :", tags)
print("artist :", artist)
print("groups :", groups)
print("languages :", languages)
print("categories :", categories)
