from selenium import webdriver 
import time
import csv 
import json
from bs4 import BeautifulSoup
import os

#       _                                      _                                #
#      | |                                    | |                               #
#   ___| |__   ___   ___  ___  ___    ___ __ _| |_ ___  __ _  ___  _ __ _   _   #
#  / __| '_ \ / _ \ / _ \/ __|/ _ \  / __/ _` | __/ _ \/ _` |/ _ \| '__| | | |  #
# | (__| | | | (_) | (_) \__ \  __/ | (_| (_| | ||  __/ (_| | (_) | |  | |_| |  #
#  \___|_| |_|\___/ \___/|___/\___|  \___\__,_|\__\___|\__, |\___/|_|   \__, |  #
#                                                       __/ |            __/ |  #
#                                                      |___/            |___/   #

category = 'movie'
user = 'raphi'

# category has to be either:                                                    #
# anime cartoon comics gaming literature movie superheroes theatre tv webcomics #

data_paths = {
    'anime':'links/ids_theatre.csv', 
    'cartoon':'links/ids_catroon.csv',
    'comics':'links/ids_comics.csv',
    'gaming':'links/ids_gaming.csv',
    'literature':'links/ids_literature.csv',
    'movie':'links/ids_movie.csv',
    'superheroes':'links/ids_superheroes.csv',
    'theatre':'links/ids_theatre.csv',
    'tv':'links/ids_tv.csv',
    'webcomics':'links/ids_webcomics.csv'}

driver_paths = {
    'nici':r'C:/Users/Harry/AppData/Local/Programs/Python/Python310/chromedriver/chromedriver.exe',
    'michelle':r'X:/YOUR/DRIVER/PATH/operadriver.exe',
    'raphi':r'C:/Users/Raphael/Documents/Universität/Master/WS 22-23/Digital Humanities/Scraping/chromedriver/chromedriver.exe'
}

# Chrome Options:
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu') 
options.add_argument("--remote-debugging-port=9222")
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.set_capability('acceptInsecureCerts', True)

# Opera Options:
# https://media.giphy.com/media/6uGhT1O4sxpi8/giphy.gif

with open(data_paths[f'{category}'], 'r') as csvfile:
    datareader = csv.reader(csvfile)
    row_count = sum(1 for row in datareader)

scrapedElements = 0

def scrape():
    global scrapedElements, category, row_count, DRIVER_PATH, user
    scrapedElements = 0
    with open(data_paths[f'{category}'], 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            id = row[0]
            
            if os.path.exists(f'profiles_subcat/{category}/{id}.json'):
                scrapedElements += 1
                continue
                
            url_profile = (f"https://api.personality-database.com/api/v1/profile/{id}")
            
            driver = webdriver.Chrome(f'{driver_paths[user]}', options=options)
            driver.get(url_profile)

            html = driver.page_source

            soup = BeautifulSoup(html, "html.parser")

            driver.close()
            try:
                pre = soup.find('pre').text
                json_pre = json.loads(pre)
            except json.JSONDecodeError as j:
                print(f'Encountered JSON-Error: {j}\nRestarting...')
                break
            except AttributeError:
                print(f'Encountered Attribute-Error: {j}\nRestarting...')
                break

            with open(f'profiles_subcat/{category}/{id}.json', 'w') as f:
                    json.dump(json_pre, f)

            scrapedElements += 1
            print(rf'Scraping ID: {id}')
            print(rf'{round((scrapedElements/row_count)*100,2)}% scraped')

while scrapedElements < row_count:
    time.sleep(1)
    scrape()