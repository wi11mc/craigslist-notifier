import subprocess
import sys
import time

subprocess.run([sys.executable, "input.py"])
time.sleep(1)
subprocess.run([sys.executable, "scraper.py"])