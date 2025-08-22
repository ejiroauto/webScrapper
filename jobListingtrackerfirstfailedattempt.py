from bs4 import BeautifulSoup
import requests
from selenium import webdriver                          #using selenium as I keep getting status code error 429. Selenium is less likely to be detected by a bot
import re
import time

driver = webdriver.Chrome()

#navigate to the website, We are scrapping a live website so a url is used. 

driver.get('https://remoteok.com/remote-python-jobs')


#This retrieves the first job post becasue job titles are in the h2 htlml tag

#driver.find_element_by_tag_name('h2')                 
 
  
