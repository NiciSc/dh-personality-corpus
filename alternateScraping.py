from urllib.request import Request, urlopen
import csv
import os
import urllib.error
import time
from header_switcher import *


headers = {
    'Host': 'api.personality-database.com',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.personality-database.com/',
    'X-TZ-Database-Name': 'Europe/Berlin',
    'Origin': 'https://www.personality-database.com',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'TE': 'trailers'
}
switcher = header_switcher()
count = 0
with open('resources/links/ids_webcomics.csv', 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        #if count == 1000:
        #    break
        if count % 10 == 0 and count > 0:
            print(rf'{count} pages scraped')
        id = row[0]
        jsonFilename = rf'profiles_subcat/webcomics/{id}.json'
        if not os.path.exists(jsonFilename):
            req = Request(rf'https://api.personality-database.com/api/v1/profile/{id}', headers = headers)
            req.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0')
            while True:
                try:
                    webpage = urlopen(req, timeout=10)
                    if webpage:
                        break;
                except urllib.error.HTTPError as e:
                    print(rf'Error: {e.code} {e.reason}')
                    print(rf'Trying again with new header...')
                    time.sleep(100)
                    req.add_header('User-Agent',rf'{switcher.switch()}')
                    continue
            # if webpage.status != 200:
            #     print(rf'Status der Anfrage: {webpage.status}')
            if(webpage.status != 403):
                myJson = open(rf'profiles_subcat/webcomics/{id}.json', 'w')
                myJson.write(webpage.read().decode('utf-8'))
        count += 1            
           
    print("Done")