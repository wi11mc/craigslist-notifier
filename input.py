import tkinter as tk
from tkinter import messagebox
import config

def SaveConfig():
    try:
        
        userURL = urlEntry.get()
        userAPIkey = apiKeyEntry.get()
        userScrapeFreq = int(scrapeFreqEntry.get())
        userMessage = messageEntry.get()
        
        with open("config.py", "w") as file:
            file.write(f"URL = '{userURL}'\n")
            file.write(f"API_KEY = '{userAPIkey}'\n")
            file.write(f"SCRAPE_FREQUENCY = {userScrapeFreq}\n")
            file.write(f"MESSAGE = '{userMessage}'\n")
            
        messagebox.showinfo("saved successfully")        
        
        
    except Exception as e:
        messagebox.showerror("error", f"{e}")
        
        
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

#scrapefrequency
scrapeFreqLabel = tk.Label(root, text="how many seconds after every scrape?:")
scrapeFreqLabel.pack()
scrapeFreqEntry = tk.Entry(root)
scrapeFreqEntry.pack()

messageLabel = tk.Label(root, text="notification message:")
messageLabel.pack()
messageEntry = tk.Entry(root)
messageEntry.pack()

#save
saveButton = tk.Button(root, text="save changes", command=SaveConfig)
saveButton.pack()

root.mainloop()