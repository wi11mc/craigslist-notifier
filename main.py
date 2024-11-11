import sys
import os
from pushbullet import Pushbullet  # Example import, replace with actual imports

# Check if the script is frozen (i.e., compiled into an executable)
if getattr(sys, 'frozen', False):
    # If frozen, the `config.py` is bundled inside the executable
    config_path = os.path.join(sys._MEIPASS, 'config.py')  # Access the bundled config file
else:
    # If not frozen, access the regular config file during development
    config_path = 'config.py'

# Dynamically load the config file
import importlib.util

spec = importlib.util.spec_from_file_location("config", config_path)
config = importlib.util.module_from_spec(spec)
spec.loader.exec_module(config)

# Now, load the API key from the config
API_KEY = config.API_KEY

# Proceed with the Pushbullet setup
pb = Pushbullet(API_KEY)

# The rest of your script goes here...
