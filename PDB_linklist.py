from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import os

# this is for clicking something
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

# nici personal driver path
DRIVER_PATH = 'C:/Users/Harry/AppData/Local/Programs/Python/Python310/chromedriver/chromedriver.exe'
URL = "https://www.personality-database.com/profile?pid=2&sort=alphabet"
page_counter = 0
max_page_count = 119

#launching the browser
chrome_options = Options()
    #chrome_options.binary_location="../Google Chrome"
    #chrome_options.add_argument("--window-size=1020,1080");
driver = webdriver.Chrome('C:/Users/Harry/AppData/Local/Programs/Python/Python310/chromedriver/chromedriver.exe', options=chrome_options)
driver.maximize_window()

driver.get(URL)

windows_before  = driver.current_window_handle
wait = WebDriverWait(driver, 10)
time.sleep(10)

# closing ad (so "next-page" can be clicked) and timer for waiting that everthing is loaded completely
close_ad = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'ezmob-footer-close'))).click()
print("ad closed")

link_list = []
#links = driver.find_elements(By.CLASS_NAME, 'profile-card-link')

while (page_counter < max_page_count):
    links = driver.find_elements(By.CLASS_NAME, 'profile-card-link')
    for link in links:
        href = link.get_attribute('href')
        link_href = {
            'link' : href
        }
        link_list.append(link_href)
    
    #time.sleep(3)    
    
    click_next_page = driver.find_element(By.CLASS_NAME, 'rc-pagination-next').click()
    #driver.execute_script("arguments[0].click();", click_next_page)
    time.sleep(3)

    page_counter +=1
    print(page_counter)
  
df = pd.DataFrame(link_list)
output_path = "C:/Users/Harry/Documents/GitHub/dh-personality-corpus/linklist_pdb.csv"
df.to_csv(output_path, mode='a', header=not os.path.exists(output_path), index=False)


#df.to_csv('linklist_superheros.csv')
#driver.close()
#driver.quit()