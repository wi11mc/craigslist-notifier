import requests
from bs4 import BeautifulSoup
import logging
import time
from pushbullet import Pushbullet



logging.basicConfig(level=logging.INFO)

API_KEY = ""
pb = Pushbullet(API_KEY)

PreviousTitle = None

def sendNoti(title, freestuff):
    pb.push_note(title, freestuff)
    logging.info("sent noti")

def theScraper():
    global PreviousTitle
    url = "https://honolulu.craigslist.org/search/big/zip#search=1~list~0~0"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        logging.info(f"successful scrape from {url}")
        soup = BeautifulSoup(response.text, 'html.parser')
    
        FirstTitle = soup.find('li', class_='cl-search-result')
    
        if FirstTitle:
            NewPost = FirstTitle.find('a', class_='posting-title').text.strip()
        
            if PreviousTitle is None or NewPost != PreviousTitle:
                logging.info(f"free stuff detected {NewPost}")
                sendNoti("free stuff", NewPost)
                PreviousTitle = NewPost
            else:
                logging.info("no new posts")
        else:
            logging.error("cant find first post.")
        
    else:
        logging.error(f"scrape failed at {url}")
    
    
while True:
    theScraper()
    time.sleep(600)