from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# this is for clicking something
from selenium.webdriver.common.action_chains import ActionChains

# nici personal driver path
DRIVER_PATH = 'C:/Users/Harry/AppData/Local/Programs/Python/Python310/chromedriver/chromedriver.exe'
URL = "https://www.personality-database.com/profile/1"

# function for 
#def launchBrowser():
chrome_options = Options()
   #chrome_options.binary_location="../Google Chrome"
chrome_options.add_argument("--window-size=1020,1080");
driver = webdriver.Chrome('C:/Users/Harry/AppData/Local/Programs/Python/Python310/chromedriver/chromedriver.exe', options=chrome_options)

driver.get(URL)

windows_before  = driver.current_window_handle
wait = WebDriverWait(driver, 10)
time.sleep(30)
#driver.close()
#char_name = wait.until(EC.visibility_of_element_located(driver.find_element(By.CLASS_NAME, "profile_name")))
print(driver.page_source)
#print(char_name)
#driver.quit()


#character_name = driver.find_element(By.XPATH, '//*[@id="root"]/div/section/main/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/h1').text

#print(driver.page_source)
#print(driver.find_element(By.XPATH, '//*[@id="root"]/div/section/main/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/h1').text)   

#while(True):
 #   pass
#launchBrowser()
