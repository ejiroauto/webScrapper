from bs4 import BeautifulSoup
import requests
import re
import time
 
time.sleep(600)                                          # This pauses execution for 30 seconds. 
url = "https://remoteok.com/remote-python-jobs"         # We are scrapping a live website so a url is used. 
response = requests.get(url)                            # This retrieves the url.
soup = BeautifulSoup(response.content, "html.parser")   # This passes the urls content to through a html reader/parser. 
print(response.status_code)                             #Check The outcome of the request. 


#jobs = soup.find('h2', attrs={'itemprop': 'title'})     # This retrieves the first job post becasue job titles are in the h2 htlml tag with an attribute of itemprop=title. 
print(response.status_code)
