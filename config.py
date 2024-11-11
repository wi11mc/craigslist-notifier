import os
import sys

if getattr(sys, 'frozen', False):  # Check if the script is frozen (i.e., compiled)
    config_path = os.path.join(sys._MEIPASS, 'config.py')  # Access the bundled config file
else:
    config_path = 'config.py'  # Access the regular config file during development

# Then load your config


URL = ""
API_KEY = ""
SCRAPE_FREQUENCY = 10
MESSAGE = ""
