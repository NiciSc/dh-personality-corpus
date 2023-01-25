from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from webdriver_manager.chrome import ChromeDriverManager
import time
import csv 
import codecs
import json
import html
from bs4 import BeautifulSoup
import os


# this is for crawling the html using selenium 
# we decided againt this method as it took more time to scrape and also as the website disconnects quicker

# nici personal driver path
DRIVER_PATH ='C:/Users/Raphael/Documents/Universität/Master/WS 22-23/Digital Humanities/Scraping/chromedriver/chromedriver.exe'
#URL = "https://www.personality-database.com/profile/1"

data_path = 'links/ids_webcomics.csv'

# coole options für chrome 
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument("--remote-debugging-port=9222")
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.set_capability('acceptInsecureCerts', True)

scrapedElements = 0

with open(data_path, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    row_count = sum(1 for row in datareader)

# über linklist iterieren
def scrape():
    with open(data_path, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        # indexzeile weglassen
        next(datareader)
        for row in datareader:
            id = row[0]
            print(id)

            if os.path.exists(f'profiles_subcat/webcomics/{id}.json'):
                continue
                
            url_profile = (f"https://api.personality-database.com/api/v1/profile/{id}")
            #url_profile = ("https://www.personality-database.com/profile/1")
            
            driver = webdriver.Chrome('C:/Users/Raphael/Documents/Universität/Master/WS 22-23/Digital Humanities/Scraping/chromedriver/chromedriver.exe', options=options)
            driver.get(url_profile)
            #char_html = driver.page_source
            time.sleep(0.1)

            html = driver.page_source

            soup = BeautifulSoup(html, "html.parser")

            driver.close()
            try:
                pre = soup.find('pre').text
                json_pre = json.loads(pre)
            except json.JSONDecodeError as j:
                print(rf'Encountered JSON Error: {j}')
                break

            with open(f'profiles_subcat/webcomics/{id}.json', 'w') as f:
                    json.dump(json_pre, f)
                    #f.write(data) this is html dump

            global scrapedElements
            scrapedElements += 1

while scrapedElements < row_count:
    time.sleep(1)
    scrape()


       

#AUSRANGIERT UND WIRD VLT NOCH GEBRAUCHT

#driver.close()
#print(driver.page_source)
#print(char_name)
#driver.quit()
#print(driver.find_element(By.XPATH, '//*[@id="root"]/div/section/main/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/h1').text)   

#while(True):
 #   pass
#launchBrowser()



#driver = webdriver.Chrome(ChromeDriverManager().install(),  chrome_options= options)
#driver.maximize_window()
#driver.get(URL)
#windows_before  = driver.current_window_handle
#wait = WebDriverWait(driver, 10).until(EC.presence_of_element_located("profile-info"))

#close_ad = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'ezmob-footer-close'))).click()




#options.add_argument('--disable-extensions')
#options.add_argument('--no-sandbox')
#options.add_argument('--disable-dev-shm-usage')
#options.add_argument("--disable-setuid-sandbox")
#options.add_argument("--disable-dev-shm-usage")



#soup = BeautifulSoup(html, 'html.parser')


# options = webdriver.ChromeOptions()
#    #chrome_options.binary_location="../Google Chrome"

# caps = webdriver.DesiredCapabilities.CHROME.copy()
# caps['acceptInsecureCerts'] = True

#'C:/Users/Harry/AppData/Local/Programs/Python/Python310/chromedriver/chromedriver.exe

        #pre_clean = pre.replace('\\', '')
        
        #data = {"{id}": [pre.text.lstrip['{'].rstrip['}'] for pre in soup.find('pre')]}