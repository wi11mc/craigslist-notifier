import requests
from bs4 import BeautifulSoup
import logging
import time
from pushbullet import Pushbullet



logging.basicConfig(level=logging.INFO)

API_KEY = ""
pb = Pushbullet(API_KEY)

PreviousFirstPostTitle = None

def sendNoti(title):
    pb.push_note(title)
    logging.info("sent noti")

def theScraper():
    url = "https://honolulu.craigslist.org/search/big/zip#search=1~gallery~0~0"
    response = requests.get(url)
    
    if response.status_code == 200:
        logging.info(f"successful scrape from {url}")
    else:
        logging.error(f"scrape failed at {url}")
        return []
    
