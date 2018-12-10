from secrets import lastFM_key,deep_dream_key
from bs4 import BeautifulSoup
from caching_protocol import Cache
import requests
import json
import sys
import urllib
import random
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

CACHE_FILE = 'project_cache.json'

def create_id(site, topic):
    return "{}_{}_{}.json".format(site, topic, str(datetime.now()).replace(' ', ''))

class Album():
    pass

def scrape_billboard():
    cache_file = CACHE_FILE
    site="Billboard"
    topic="top album sales"
    cache = Cache(cache_file)
    base = "https://www.billboard.com/charts/top-album-sales"
    UID = create_id(site, topic)
    response = cache.get(UID)

    if response == None:
        response = requests.get(base).text
        cache.set(UID, response, 7)

    soup = BeautifulSoup( response, 'html.parser')
    #links = soup.find_all('a')
    #for t in links:

    #return something
    return None

def get_album_covers():
    pass

def deep_dream():
    pass

def make_collage():
    pass




process(response)
