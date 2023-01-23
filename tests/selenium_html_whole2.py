from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv 
import codecs
import json
import html
from bs4 import BeautifulSoup



# this is for crawling the html using selenium 
# we decided againt this method as it took more time to scrape and also as the website disconnects quicker

# nici personal driver path
DRIVER_PATH = 'C:/Users/Harry/AppData/Local/Programs/Python/Python310/chromedriver/chromedriver.exe'
#URL = "https://www.personality-database.com/profile/1"

data_path = 'links/webcom2.csv'

# coole options für chrome 
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument("--remote-debugging-port=9222")
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.set_capability('acceptInsecureCerts', True)

# über linklist iterieren
with open(data_path, 'r') as csvfile:
    datareader = csv.reader(csvfile)

    # indexzeile weglassen
    next(datareader)
    for row in datareader:
        id = row[0]
        print("id" + id)
        
        url_profile = (f"https://www.personality-database.com/profile/{id}")
        #url_profile = ("https://www.personality-database.com/profile/1")
        
        driver = webdriver.Chrome('C:/Users/Harry/AppData/Local/Programs/Python/Python310/chromedriver/chromedriver.exe', options=options)
        driver.get(url_profile)
        #char_html = driver.page_source
        time.sleep(10)
        #char_content = driver.find_element(By.CLASS_NAME, 'profile-detail').text
        #print("row " + row[0])
        #print(char_html)
        #print("char_content" + char_content)

        html = driver.page_source
        driver.close()

        soup = BeautifulSoup(html, "html.parser")

        #extrahieren der teile wir wollen (so wie ich das auch ursprünglich machen wollte, das ist dann direkt beim scrapen schon bissl aufgeräumt)
        char_name = soup.find('div', class_ = 'rc-col rc-col-8 rc-col-sm-12').text #.encode('utf-8')
        personality_quick_info = soup.find('div', class_ = 'profile-personality').text
        medium_name_par = soup.find('a', class_ = 'link')
        medium_name = medium_name_par.find_next('h1').text
        last_update = soup.find('span', class_ = 'last-update').text.split(': ')[1]
        cut_last_update = last_update
    
        #optionale info
        added_by = soup.find('label', class_ = 'contributor')
        if added_by is not None:
            added_by = added_by.get_text().split('Added by ')[1]
        else:
            added_by = ''

        #more_media = soup.find('span', class_ = 'group-name').next_element.next_element.next_element.next_element
        #print(more_media)
        # works = more_media[1].next.text
        # acting = more_media[2].text

        total_votes_count = soup.find('h2').text.split(' Votes')[0]
        
        mbti_letters = soup.findAll('label', class_ = 'letter')
        mbti_percentages = soup.findAll('label', class_ = 'percent')

        mbti_energy_letter = mbti_letters[0].text
        mbti_energy_percent = mbti_percentages[0].text
        mbti_attention_letter = mbti_letters[1].text
        mbti_attention_percent = mbti_percentages[1].text
        mbti_decision_letter = mbti_letters[2].text
        mbti_decision_percent = mbti_percentages[2].text
        mbti_living_letter = mbti_letters[3].text
        mbti_living_percent = mbti_percentages[3].text


        mbti_values = {
            'mbti_energy_letter' : mbti_energy_letter,
            'mbti_energy_percent' : mbti_energy_percent, 
            'mbti_attention_letter' : mbti_attention_letter,
            'mbti_attention_percent' : mbti_attention_percent,
            'mbti_decision_letter' : mbti_decision_letter,
            'mbti_decision_percent' : mbti_decision_percent, 
            'mbti_living_letter' : mbti_living_letter,
            'mbti_living_percent' : mbti_living_percent,


        }

        data = {
            'id' : id,
            'name' : char_name,
            'personality_quick_info' : personality_quick_info,
            'medium_name' : medium_name,
            'last_update' : cut_last_update,
            'added_by' : added_by,
            #'works' : works
            'total_votes_count' : total_votes_count,
            'mbti' : mbti_values

        }

        with open(f'profiles_subcat/webcomics3/{id}.json', 'w') as f:
                json.dump(data, f)

    
        


       

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