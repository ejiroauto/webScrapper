from bs4 import BeautifulSoup
import requests
from selenium import webdriver                          #using selenium as I keep getting status code error 429. Selenium is less likely to be detected by a bot
import re
import time
 
time.sleep(350)                                         # This pauses execution for 350 seconds approx 5 mins. 
url = "https://remoteok.com/remote-python-jobs"         # We are scrapping a live website so a url is used. 
response = requests.get(url)                            # This retrieves the url.
soup = BeautifulSoup(response.content, "html.parser")   # This passes the urls content to through a html reader/parser. 
print(response.status_code)                             # Check The outcome of the request. I keep getting 429 


#jobs = soup.find('h2', attrs={'itemprop': 'title'})     # This retrieves the first job post becasue job titles are in the h2 htlml tag with an attribute of itemprop=title. 
print(response.status_code)
