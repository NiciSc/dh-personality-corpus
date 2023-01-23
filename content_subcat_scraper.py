import requests
import json
import csv
import os
import time
from header_switcher import *

newCSV = rf'profiles_subcat/webcomics/webcomics errorList.csv'
count = 0
# The request pretends to come from Chrome instead of Python to avoid 403 HTTP response (forbidden) and "'content_char' is not defined" error
switcher = header_switcher()
headers = switcher.switch()
session = requests.Session()
with open('resources/links/ids_webcomics.csv', 'r') as csvfile: #'links/ids_webcomics.csv'
    datareader = csv.reader(csvfile)
    for row in datareader:
        if count == 1000:
            break
        if count % 10 == 0 and count > 0:
            print(rf'{count} pages scraped')
        id = row[0].split('/')[-1]
        jsonFilename = rf'profiles_subcat/webcomics/{id}.json'
        if not os.path.exists(jsonFilename):
            print(f'Request with header: {headers}')
            response = session.get(rf"https://api.personality-database.com/api/v1/profile/{id}", headers=headers)

            print(f"Response-Code for initial Request: {response.status_code}")

            if response.status_code == 403:
                startTime = time.time()
                print('Website forbids scraping, retrying...')
                code = 403
                while code == 403:
                    headers = switcher.switch()
                    print(rf'Trying to establish connection...')
                    for i in range(300):
                        time.sleep(1)
                        if i % 5 == 0:
                            print(i,end=" ")
                    print(rf'Request with header: {headers}')
                    newresponse = session.get(rf"https://api.personality-database.com/api/v1/profile/{id}", headers = headers)
                    code = newresponse.status_code
                print(f'New Response Code is: {code}')
                print(rf'Time for reconnect is {time.time() - startTime} Seconds')
            else:
                if response.status_code != 204:
                    '''response.status_code != 204 and
                    response.headers["content-type"].strip().startswith("application/json")
                ):'''
                    try:
                        content_char = response.json()
                    except ValueError:
                        print("ValueError")
                with open(jsonFilename, 'w') as f:
                    json.dump(content_char, f)
                count += 1            
                # while response.status_code == 403:
                #     print('Website forbids scraping, retrying with new header...')
                #     newResponse = requests.get(rf"https://api.personality-database.com/api/v1/profile/{id}", headers = switcher.switch())
                #     print(rf'Website responds to new header with {newResponse.status_code}')
                #     time.sleep(1)
            #assert(response.status_code != 403)
            # if (
            #     response.status_code != 204 and
            #     response.headers["content-type"].strip().startswith("application/json")
            # ):
            #     try:
            #         content_char = response.json()
            #     except ValueError:
            #         print("ValueError")

            # decide how to handle a server that's misbehaving to this extent            
            # with open(jsonFilename, 'w') as f:
            #     json.dump(content_char, f)
            
            # count += 1
    print("Done")