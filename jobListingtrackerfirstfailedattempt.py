from bs4 import BeautifulSoup
import requests
from selenium import webdriver              #using selenium as I keep getting status code error 429, with requests lib. Selenium is less likely to be detected by a bot.
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import time

driver = webdriver.Chrome()
type(driver)

#Let the user actually see something! 

time.sleep(5) 

#navigate to the website, We are scrapping a live website so a url is used. 

driver.get('https://remoteok.com/')

# Locate the input field by its ID
search_field = driver.find_element(By.CLASS_NAME, 'search')

# Enter text into the input field
search_input = search_field.send_keys('Python')

#Hit Enter 
search_enter = search_field.send_keys(Keys.ENTER)


#This retrieves the first job post becasue job titles are in the h2 htlml tag

jobs = driver.find_element(By.TAG_NAME, 'h2')                


print(jobs)
