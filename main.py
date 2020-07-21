from telegraph import Telegraph
import scrape
from argparse import ArgumentParser

parser = ArgumentParser(description="Script to give you allow you to easily read doujins as telegraph articles")
parser.add_argument("-s", "--source", help="The digits of the doujin", type=int)
args = parser.parse_args()

if not args.source:
    print("Please provide source to scrape")
    exit(1)

title, data, image_tags,= scrape.get_info(args.source)

telegraph = Telegraph()

telegraph.create_account(short_name='nhentai_bot')
article_path = telegraph.create_page(title, html_content=image_tags)['path']

print("title :", title)
for key, value in data.items():
    if value:
        print(key,": ",value,"\n")
print("Path: ",'https://telegra.ph/{}'.format(article_path))
