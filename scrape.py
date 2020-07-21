from string import Template
from bs4 import BeautifulSoup
import requests

def get_info(digits):
    # generate soup object for doujin
    soup = BeautifulSoup(requests.get(f"https://nhentai.net/g/{digits}/").text, 'html.parser')

    title = soup.find('h1').text  # title
    title_jap = soup.find('h2').text  # title in japnese
    article = soup.find("h3", {"id": "gallery_id"}).text  # hash id
    # get gallery ID for the doujin pages
    thumbnail = soup.find("meta", {"itemprop": "image"})
    gallery_id = thumbnail.get('content').split("/")[-2]

    content = soup.find_all("div", {"class": "tag-container"})  # scrape tag container

    parodies = get_content(content, 0)
    characters = get_content(content, 1)
    tags = get_content(content, 2)
    artist = "#" + content[3].find("span", {"class": "name"}).text.replace(' ', '_').replace('-', '_').replace('.', '_')
    groups = get_content(content, 4)
    languages = get_content(content, 5)
    categories = get_content(content, 6)
    pages = content[7].find("span", {"class": "name"}).text

    image_template = Template('<img src="https://i.nhentai.net/galleries/$gallery_id/$page_no.$image_type">')

    image_tags = ""

    for page_no in range(1, int(pages) + 1):
        pg_img = soup.find('a', {'href': f"/g/{digits}/{page_no}/"}).find('img')
        image_type = pg_img.get('data-src').split(".")[-1]
        image_tags += (
            image_template.substitute({'gallery_id': gallery_id, 'page_no': page_no, 'image_type': image_type}) + "\n"
        )

    return (
        title,
        {
            'Title' : title_jap,
            'Article' : article,
            'Parodies': parodies,
            'Characters': characters,
            'Tags': tags,
            'Artists': artist,
            'Groups': groups,
            'Languages': languages,
            'Categories': categories,
        },
        image_tags,
    )

def get_content(content, id):
    info = content[id].find_all("span", {"class": "name"})

    items = []
    for i in range(len(info)):
        items.append(info[i].text)

    if not items:
        return None
    else:
        res = ""
        for item in items:
            res += f"#{item.replace(' ', '_').replace('-', '_').replace('.', '')} "
        return res.strip()
