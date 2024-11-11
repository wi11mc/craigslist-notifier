import requests
from bs4 import BeautifulSoup
import logging
import time
from pushbullet import Pushbullet
from config import URL, API_KEY, SCRAPE_FREQUENCY, MESSAGE
from notifications import SendNotification


logging.basicConfig(level=logging.INFO)

pb = Pushbullet(API_KEY)

#the previous title gets saved as a vairable in the memory rather than as a file
PreviousTitle = None

def theScraper():
    global PreviousTitle
    
    response = requests.get(URL)
    
    if response.status_code == 200:
        logging.info(f"successful scrape from {URL}")
        soup = BeautifulSoup(response.text, 'html.parser')
    
    #only the first and previous title will be parsed to save memory
    
        FirstTitle = soup.find('li', class_='cl-search-result')
    
        if FirstTitle:
            NewPost = FirstTitle.find('a', class_='posting-title').text.strip()
        
            if PreviousTitle is None or NewPost != PreviousTitle:
                logging.info(f"free stuff detected {NewPost}")
                SendNotification(MESSAGE, NewPost)
                PreviousTitle = NewPost

            else:
                logging.info("no new posts")
        else:
            logging.warning("no new free stuff")
        
    else:
        logging.error(f"scrape failed at {URL} status code: {response.status_code}")
    
    
while True:
    theScraper()
    time.sleep(SCRAPE_FREQUENCY)