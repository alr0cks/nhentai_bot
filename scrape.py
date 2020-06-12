import requests
from bs4 import BeautifulSoup
import re

url = "https://nhentai.net/g/39471/"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')


def get_info(soup, url):
    title1 = soup.find('h1').text   #title
    title2 = soup.find('h2').text   #title in japnese
    article = soup.find("h3",{"id":"gallery_id"}).text      #hash id

    content = soup.find_all("div",{"class":"tag-container"})    #scrape tag container
    
    Parodies = get_content(content, 0)
    Characters = get_content(content, 1)
    Tags = get_content(content, 2)
    Artist = get_content(content, 3)
    Groups = get_content(content, 4)
    Languages = get_content(content, 5)
    Categories = get_content(content, 6)
    Pages = get_content(content, 7)
    img_list = []

    for i in range(1,int(Pages[0])):             #get images url
        new_url = url + str(i)
        # print(new_url)
        img_list.append(get_image(new_url))
    
    # print("Parodies: {}".format(', '.join(Parodies)))
    # print("Characters: {}".format(', '.join(Characters)))
    # print("Tags: {}".format(', '.join(Tags)))
    # print("Artist: {}".format(', '.join(Artist)))
    # print("Groups: {}".format(', '.join(Groups)))
    # print("Languages: {}".format(', '.join(Languages)))
    # print("Categories: {}".format(', '.join(Categories)))
    # print("Pages: {}".format(', '.join(Pages)))
    # # print("Images: {}".format(', '.join(img_list)))

    temp = "Parodies: {}".format(', '.join(Parodies) + "\n" + "Characters: {}".format(', '.join(Characters))) + "\n" + "Artist: {}".format(', '.join(Artist)) + "\n" + "Tags: {}".format(', '.join(Tags)) + "\n" + "Groups: {}".format(', '.join(Groups)) + "\n" + "Languages: {}".format(', '.join(Languages)) + "\n" + "Categories: {}".format(', '.join(Categories)) + "\n" + "Pages: {}".format(', '.join(Pages)) + "\n" + "Images: {}".format(', '.join(img_list))
    # print(temp)

    return temp
       
    


def get_content(content, id):
    info = content[id].find_all("span",{"class":"name"})
    list = []
    for i in range(len(info)):
        list.append(info[i].text)

    # print(list)
    if not list:
        return None
    else:
        return list
    # return list

def get_image(url):
    r = requests.get(url)
    soup_img = BeautifulSoup(r.text, 'html.parser')
    images = soup_img.find_all('img', {'src':re.compile('.jpg')})
    for image in images: 
        # print(image['src'])
        return (image['src'])


     
    

# info = get_info(soup,url)
# print(info)

    
