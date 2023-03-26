import urllib
import requests
#import re
#import os
from bs4 import BeautifulSoup

# Test for scraping Personaility-Database.com using Beautiful Soup
# Unfortunately not working, as Webpage is rendered on the client-side -> next test using Selenium

url = requests.get('https://www.personality-database.com/profile/1/jerry-seinfeld-seinfeld-mbti-personality-type')
soup = BeautifulSoup(url.content, 'html.parser')

character_name = soup.find(class_ = 'profile-name').text

print(character_name)