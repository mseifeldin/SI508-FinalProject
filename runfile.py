from secrets import deep_dream_key
from bs4 import BeautifulSoup
from caching_protocol import Cache
import requests
import json
import sys
import urllib
import random
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from path_settings import project_path, local_path

CACHE_FILE = 'project_cache.json'
image_directory = project_path + local_path
collage_directory = image_directory + "collage.jpg"
dream_directory = image_directory + "dream.jpg"
##############################################################################################

####################################################
################CLASSES
####################################################

class Album():
    def __init__(self, album, artist):
        self.album = album
        self.artist = artist

    def getalbum(self):
        return self.album
    def getartist(self):
        return self.artist


class AlbumImage(Album):
    def __init__(self, album, artist, url):
        Album.__init__(self,album, artist)
        self.url = url

    def geturl(self):
        return self.url

####################################################
################FUNCTIONS
####################################################

def create_id(site, topic):
    return "{}_{}_{}.json".format(site, topic, str(datetime.now()).replace(' ', ''))

def scrape_billboard():
    cache_file = CACHE_FILE
    site="Billboard"
    topic="top album sales"
    cache = Cache(CACHE_FILE)
    base = "https://www.billboard.com/charts/top-album-sales"
    UID = create_id(site, topic)
    response = cache.get(UID)
    list_of_albums = []

    if response == None:
        response = requests.get(base).text
        cache.set(UID, response, 7)

    soup = BeautifulSoup( response, 'html.parser')

    topalbum = soup.find("div", {'class':"chart-number-one__title"}).text
    topalbum = topalbum.strip()
    topartist = soup.find("div", {'class':"chart-number-one__artist"}).text
    topartist = topartist.strip()
    topalbumdata = Album(topalbum, topartist)
    list_of_albums.append(topalbumdata)

    albums = soup.find_all("div", {'class':"chart-list-item__text"})
    for album in albums:
        albumname = album.find('span', class_='chart-list-item__title-text').text
        albumname = albumname.strip()
        artistname = album.find('div', class_='chart-list-item__artist').text
        artistname = artistname.strip()

        albumdata = Album(albumname, artistname)
        list_of_albums.append(albumdata)

    return list_of_albums

def get_album_covers(albumdata):
    baseurl = "https://itunes.apple.com/search"
    site = "iTunes"
    cache = Cache(CACHE_FILE)
    image_list = []
    for album in albumdata:
        topic = str(album.getalbum())
        UID = create_id(site, topic)
        itunes_data = cache.get(UID)
        try:
            if itunes_data == None:
                params_diction = {}
                params_diction["term"] = album.getartist()
                params_diction["entity"] = "album"
                itunes_data = requests.get(baseurl, params=params_diction)
                itunes_data = itunes_data.json()
                cache.set(UID, itunes_data, 7)
                for i in itunes_data["results"]:
                    if i["collectionName"] == str(album.getalbum()):
                        imageurl = i["artworkUrl100"]
                        image = AlbumImage(album.getalbum(), album.getartist(), imageurl)
                        image_list.append(image)
        except:
            continue
    return image_list


def download_image(url , albumimage, directory):
    path = directory + albumimage.getalbum() + albumimage.getartist() + '.jpg'
    urllib.request.urlretrieve(url , path)
    return path

def download_album_images(image_list):
    image_info = []
    for image in image_list:
        url = image.geturl()
        path = download_image(url , image , image_directory)
        spot_info = {
            'name': image.getalbum(),
            'artist': image.getartist(),
            'path': path,
            }
        image_info.append(spot_info)
    return image_info


def create_collage(cells, cols=5, rows=5):
    w, h = Image.open(cells[0]['path']).size
    collage_width = cols * w
    collage_height = rows * h
    new_image = Image.new('RGB', (collage_width, collage_height))
    cursor = (0,0)
    for cell in cells:
        # place image
        new_image.paste(Image.open(cell['path']), cursor)


        # move cursor
        y = cursor[1]
        x = cursor[0] + w
        if cursor[0] >= (collage_width - w):
            y = cursor[1] + h
            x = 0
        cursor = (x, y)

    new_image.save(collage_directory)

def deep_dream(verbose):
    baseurl = "https://api.deepai.org/api/deepdream"
    site = "DeepDream"
    cache = Cache(CACHE_FILE)
    topic = "dreaming"
    UID = create_id(site, topic)
    dream_response = cache.get(UID)
    if dream_response == None:
        r = requests.post(baseurl,files={'content': open(collage_directory, 'rb'),},headers={'api-key': deep_dream_key})
        dream_response= r.json()
        cache.set(UID, dream_response, 7)
    dream_url = dream_response["output_url"]
    urllib.request.urlretrieve(dream_url, dream_directory)
    im = Image.open(dream_directory)
    if verbose == "yes":
        im.show()
    return dream_url

def list_albums(imagelist, dummy = "no"):
    printlist = []
    if dummy == "no":
        print("ALBUMS IN THE IMAGE:")
    for i in imagelist:
        print_statement = ("{} by {}".format(i["name"], i["artist"]))
        printlist.append(print_statement)
        if dummy == "no":
            print(print_statement)
    return printlist


##############################################################################################

####################################################
################RUN CODE
####################################################

print("scraping Billboard top albums...")
albumdata = scrape_billboard()
print("scraping done")
print("getting album info...")
image_list = get_album_covers(albumdata)
print("album info retrieved")
print("downloading album images...")
images = download_album_images(image_list)
print("album images downloaded")
collage_images = []
for i in images:
    if i not in collage_images:
        collage_images.append(i)
collage_images = collage_images[:25]
print("creating collage...")
create_collage(collage_images, cols=5, rows=5)
print("collage created and saved")
print("generating deep dream image...")
deep_dream("yes")
list_albums(collage_images)
