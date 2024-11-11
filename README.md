# Craigslist Notifier
a simple python script to scrape craigslist free section and send push notifications to my phone or computer. the push API used is called push bullet and it is free

the idea was to put all of this into pyinstaller so you can run it as a executable and not have to download all of the dependencies. for some reason since it has to run the tkinter window with input.py first to get your personal configuarment input like the url you want to scrape, your api key, your scrape frequency and your notification message. and once all of the personal data has been recorded into config.py the scraper was supposed to automatically start with the users configuration settings.

it does not work when compiled. perhaps it needs more of a main tkinter window to start and stop the scraper and edit the configuration input. it might be because I dont know how to make it so that it works in synchrony one process after the other.

I will come back to this and redo all of this later because I actually need to be able to use it to get free stuff on craigslist.
