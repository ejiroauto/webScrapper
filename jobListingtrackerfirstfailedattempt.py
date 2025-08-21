from bs4 import BeautifulSoup
import requests
import re
import time
 
time.sleep(30)                                          # This pauses execution for 30 seconds. 
url = "https://remoteok.com/remote-python-jobs"         # We are scrapping a live website so a url is used. 
response = requests.get(url)                            # This retrieves the url.
soup = BeautifulSoup(response.content, "html.parser")   # This passes the urls content to through a html reader/parser. 

jobtitles = soup.find_all('h2', class_= 'title')           # This retrieves all the jobs post containing python as when I inspected the web page it was in a h2 container. - this did not print anything. 
for jobtitles in jobtitles:
    print(jobtitles.text)
