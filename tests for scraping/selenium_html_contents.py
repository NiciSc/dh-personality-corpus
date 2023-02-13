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
URL = "https://www.personality-database.com/profile/495096"

# function for 
#def launchBrowser():
chrome_options = Options()
   #chrome_options.binary_location="../Google Chrome"
chrome_options.add_argument("--window-size=1020,1080");
driver = webdriver.Chrome('C:/Users/Harry/AppData/Local/Programs/Python/Python310/chromedriver/chromedriver.exe', options=chrome_options)

driver.get(URL)

windows_before  = driver.current_window_handle
wait = WebDriverWait(driver, 10)
time.sleep(10)
#driver.close()
#print(driver.page_source)
#print(char_name)
#driver.quit()


character_name = driver.find_element(By.XPATH, '//*[@id="root"]/div/section/main/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/h1').text
character_mbti_energy_letter = driver.find_element(By.XPATH, '//*[@id="root"]/div/section/main/div[1]/div[2]/div/div[1]/div[1]/div[6]/div/div[1]/div[1]/div[1]/div[1]/label[2]').text
character_mbti_energy_percent = driver.find_element(By.XPATH, '//*[@id="root"]/div/section/main/div[1]/div[2]/div/div[1]/div[1]/div[6]/div/div[1]/div[1]/div[1]/div[1]/label[1]').text
character_mbti_attention_letter = driver.find_element(By.XPATH, '//*[@id="root"]/div/section/main/div[1]/div[2]/div/div[1]/div[1]/div[6]/div/div[1]/div[1]/div[1]/div[2]/label[2]').text
character_mbti_attention_percent = driver.find_element(By.XPATH, '//*[@id="root"]/div/section/main/div[1]/div[2]/div/div[1]/div[1]/div[6]/div/div[1]/div[1]/div[1]/div[2]/label[1]').text
character_mbti_decision_letter = driver.find_element(By.XPATH, '//*[@id="root"]/div/section/main/div[1]/div[2]/div/div[1]/div[1]/div[6]/div/div[1]/div[1]/div[1]/div[3]/label[2]').text
character_mbti_decision_percent = driver.find_element(By.XPATH, '//*[@id="root"]/div/section/main/div[1]/div[2]/div/div[1]/div[1]/div[6]/div/div[1]/div[1]/div[1]/div[3]/label[1]').text
character_mbti_living_letter = driver.find_element(By.XPATH, '//*[@id="root"]/div/section/main/div[1]/div[2]/div/div[1]/div[1]/div[6]/div/div[1]/div[1]/div[1]/div[4]/label[2]').text
character_mbti_living_percent = driver.find_element(By.XPATH, '//*[@id="root"]/div/section/main/div[1]/div[2]/div/div[1]/div[1]/div[6]/div/div[1]/div[1]/div[1]/div[4]/label[1]').text
print(character_name)
print(character_mbti_energy_letter, character_mbti_energy_percent)
print(character_mbti_attention_letter, character_mbti_attention_percent)
print(character_mbti_decision_letter, character_mbti_decision_percent)
print(character_mbti_living_letter, character_mbti_living_percent)

#print(driver.page_source)
#print(driver.find_element(By.XPATH, '//*[@id="root"]/div/section/main/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/h1').text)   

#while(True):
 #   pass
#launchBrowser()
