import requests
from bs4 import BeautifulSoup
import logging
import time
from pushbullet import Pushbullet
import config
from notifications import SendNotification
import subprocess
import sys
import os
import atexit

URL = config.URL
API_KEY = config.API_KEY
SCRAPE_FREQUENCY = config.SCRAPE_FREQUENCY
MESSAGE = config.MESSAGE

# Logging configuration
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("scraper_errors.log")
    ]
)

lock_file = "scraper.lock"

# Ensure only one instance of the scraper runs at a time
def check_single_instance():
    if os.path.exists(lock_file):
        logging.info("Another instance is already running. Exiting.")
        sys.exit(0)
    else:
        # Use 'with' to automatically close the file after use
        with open(lock_file, 'w') as f:
            pass

# Function to clean up the lock file on exit
def remove_lock_file():
    if os.path.exists(lock_file):
        os.remove(lock_file)

# Register the cleanup function to be run on exit
atexit.register(remove_lock_file)

# Ensure single instance before starting
check_single_instance()

# Attempt to load configuration
try:
    from config import URL, API_KEY, SCRAPE_FREQUENCY, MESSAGE
except (ImportError, AttributeError) as e:
    logging.error(f"Configuration error: {e}")
    subprocess.run([sys.executable, "input.py"])  # Run input.py to gather configuration
    logging.info("Please restart the application after entering the configuration.")
    sys.exit(0)  # Exit after running input.py

# Initialize Pushbullet API
pb = Pushbullet(API_KEY)

# Previous post title to track changes
PreviousTitle = None

def theScraper():
    global PreviousTitle

    try:
        response = requests.get(URL)

        if response.status_code == 200:
            logging.info(f"Successful scrape from {URL}")
            soup = BeautifulSoup(response.text, 'html.parser')

            # Only parse the first post and previous title to save memory
            FirstTitle = soup.find('li', class_='cl-search-result')

            if FirstTitle:
                NewPost = FirstTitle.find('a', class_='posting-title').text.strip()

                if PreviousTitle is None or NewPost != PreviousTitle:
                    logging.info(f"Free stuff detected: {NewPost}")
                    SendNotification(MESSAGE, NewPost)
                    PreviousTitle = NewPost
                else:
                    logging.info("No new posts.")
            else:
                logging.warning("No new free stuff.")
        else:
            logging.error(f"Scrape failed at {URL} - Status code: {response.status_code}")
    
    except Exception as e:
        logging.exception(f"An error occurred during scraping: {e}")
        time.sleep(5)  # Wait for 5 seconds before retrying if an error occurs

# Main loop
while True:
    theScraper()
    time.sleep(SCRAPE_FREQUENCY)
