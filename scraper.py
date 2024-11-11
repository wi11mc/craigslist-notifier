import requests
from bs4 import BeautifulSoup
import logging
import time
from pushbullet import Pushbullet
from config import URL, API_KEY, SCRAPE_FREQUENCY



logging.basicConfig(level=logging.INFO)

pb = Pushbullet(API_KEY)

#the previous title gets saved as a vairable in the memory rather than as a file
PreviousTitle = None

def sendNoti(title, freestuff):
    pb.push_note(title, freestuff)
    logging.info("sent noti")

def theScraper():
    global PreviousTitle
    
    response = requests.get(URL)
    
    if response.status_code == 200:
        logging.info(f"successful scrape from {url}")
        soup = BeautifulSoup(response.text, 'html.parser')
    
    #only the first and previous title will be parsed to save memory
    
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
    time.sleep(SCRAPE_FREQUENCY)