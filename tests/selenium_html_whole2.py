from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv 
import codecs


# this is for crawling the html using selenium 
# we decided againt this method as it took more time to scrape and also as the website disconnects quicker

# nici personal driver path
DRIVER_PATH = 'C:/Users/Harry/AppData/Local/Programs/Python/Python310/chromedriver/chromedriver.exe'
URL = "https://www.personality-database.com/profile/1"

data = 'links_short.csv'



chrome_options = Options()
   #chrome_options.binary_location="../Google Chrome"
chrome_options.add_argument("--window-size=1020,1080");
driver = webdriver.Chrome('C:/Users/Harry/AppData/Local/Programs/Python/Python310/chromedriver/chromedriver.exe', options=chrome_options)
driver.maximize_window()
driver.get(URL)

windows_before  = driver.current_window_handle
wait = WebDriverWait(driver, 10)

close_ad = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'ezmob-footer-close'))).click()
print("ad closed")

time.sleep(10)


with open(data, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        driver.get(row)
        #char_html = driver.page_source
        time.sleep(30)
        char_content = driver.find_element(By.CLASS_NAME, 'rc-col rc-col-8 rc-col-sm-12').decode('unicode')
        print(row)
        #print(char_html)
        print(char_content)

       



#driver.close()
#print(driver.page_source)
#print(char_name)
#driver.quit()
#print(driver.find_element(By.XPATH, '//*[@id="root"]/div/section/main/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/h1').text)   

#while(True):
 #   pass
#launchBrowser()
