import tkinter as tk
from tkinter import messagebox
import config

def SaveConfig():
    try:
        
        userUrl = urlEntry.get()
        userAPIkey = ApiKeyEntry.get()
        userScrapeFreq = int(ScrapeFreqEntry.get())
        userMessage = MessageEntry.get()
        
        with open("config.py", "w") as file:
            file.write(f"URL = '{userURL}'\n")
            file.write(f"API_KEY = '{userAPIkey}'\n")
            file.write(f"SCRAPE_FREQUENCY = {userScrapeFreq}\n")
        
        
        
    except Exception as e:
        messagebox.showerror("error: {e}")
        
        
root =tk.Tk()
root.title("configure the scraper")


#url
urlLabel = tk.Label(root, text="craigslist URL:")
urlLabel.pack()
urlEntry = tk.Entry(root)
urlEntry.pack()


#api
apiKeyLabel = tk.Label(root, text="pushbullet API key:")
apiKeyLabel.pack()
apiKeyEntry = tk.Entry(root)
apiKeyEntry.pack()


saveButton = tk.Button(root, text="save changes", command=SaveConfig)
saveButton.pack()

root.mainloop()