from pushbullet import Pushbullet
import logging
from config import API_KEY

pb = Pushbullet(API_KEY)

def SendNotification(title, message):
    try:
        pb.push_note(title, message)
        logging.info(f"notification sent: {title} - {message}")
    except Exception as e:
        logging.error(f"failed to send noti: {e}")