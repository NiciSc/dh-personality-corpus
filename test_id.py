import requests
import json
import pandas as pd
import os

offset = 0
ids = []
url = "https://www.personality-database.com/profile/"

while (offset < 1100000):
    
    response = requests.get(f"https://api.personality-database.com/api/v1/profiles?offset={offset}&limit=500&pid=2&sort=alphabet&property_id=2")
    #print(response.status_code)
    offset += 500

    #print(response.json())


    def jprint(obj):
         text = json.dumps(obj, sort_keys=True, indent=4)
         #print(text)


    profiles = response.json()["profiles"]
    for profile in profiles:
        id = profile['id']
        ids.append(url + str(id))
    #jprint(ids)

    offset += 500
    print(offset)


df = pd.DataFrame(ids)
output_path = "C:/Users/Harry/Documents/GitHub/dh-personality-corpus/id_list.csv"
df.to_csv(output_path, mode='a', header=not os.path.exists(output_path), index=False)


#jprint(response.json())