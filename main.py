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
) = scrape.get_info(source)

telegraph = Telegraph()

telegraph.create_account(short_name='nhentai_bot')
article_path = telegraph.create_page(title, html_content=image_tags)['path']

print('https://telegra.ph/{}'.format(article_path))
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
