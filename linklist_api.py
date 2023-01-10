import requests
import json
import pandas as pd
import os

offset = 0
ids = []
url = "https://www.personality-database.com/profile/"

while (offset < 10500):

    # alphabetisch
    #response = requests.get(f"https://api.personality-database.com/api/v1/profiles?offset={offset}&limit=500&pid=2&sort=alphabet&property_id=2")
    # print(response.status_code)

    # nach hot
   # anime 8
   # gaming 11
   # cartoons 7
   # literature 12 
   # comics 9
   # webcomics 26
   # theare 13

    # urls for requests, change sorting to new, top, hot, alphabetical for more variety
    #response = requests.get(f"https://api.personality-database.com/api/v1/profiles?offset={offset}&limit=500&pid=2&sort=alphabet&property_id=2")
    #response = requests.get(f"https://api.personality-database.com/api/v1/profiles?offset={offset}&limit=500&cid=27&pid=2&sort=alphabet&cat_id=27&property_id=2")
    #response = requests.get(f"https://api.personality-database.com/api/v1/profiles?offset={offset}&limit=500&cid=3&pid=2&sort=alphabet&cat_id=3&property_id=2")
    #response = requests.get(f"https://api.personality-database.com/api/v1/profiles?offset={offset}&limit=500&cid=2&pid=2&sort=alphabet&cat_id=2&property_id=2")
    #response = requests.get(f"https://api.personality-database.com/api/v1/profiles?offset={offset}&limit=500&cid=2&pid=2&sort=alphabet&cat_id=2&property_id=2")
    #response = requests.get(f"https://api.personality-database.com/api/v1/profiles?offset={offset}&limit=500&cid=8&pid=2&sort=alphabet&cat_id=8&property_id=2")
    #response = requests.get(f"https://api.personality-database.com/api/v1/profiles?offset={offset}&limit=500&cid=26&pid=2&sort=alphabet&cat_id=26&property_id=2")
    #response = requests.get(f"https://api.personality-database.com/api/v1/profiles?offset={offset}&limit=500&cid=11&pid=2&sort=alphabet&cat_id=11&property_id=2")
    #response = requests.get(f"https://api.personality-database.com/api/v1/profiles?offset={offset}&limit=500&cid=7&pid=2&sort=alphabet&cat_id=7&property_id=2")
    #response = requests.get(f"https://api.personality-database.com/api/v1/profiles?offset={offset}&limit=500&cid=12&pid=2&sort=alphabet&cat_id=12&property_id=2")
    #response = requests.get(f"https://api.personality-database.com/api/v1/profiles?offset={offset}&limit=500&cid=9&pid=2&sort=alphabet&cat_id=9&property_id=2")
    #response = requests.get(f"https://api.personality-database.com/api/v1/profiles?offset={offset}&limit=500&cid=13&pid=2&sort=alphabet&cat_id=13&property_id=2")
    response = requests.get(f"https://api.personality-database.com/api/v1/profiles?offset={offset}&limit=500&pid=2&sort=alphabet&property_id=2")
   
    profiles = response.json()["profiles"]

    for profile in profiles:
        id = profile['id']
        ids.append(url + str(id))
        #print(id)

    # größtes intervall das geht = 500
    offset += 500
    print(offset)

#print(ids)

df = pd.DataFrame(ids)
output_path = "C:/Users/Harry/Documents/GitHub/dh-personality-corpus/id_list.csv"
df.to_csv(output_path, mode='a', header=not os.path.exists(output_path), index=False)


#jprint(response.json())