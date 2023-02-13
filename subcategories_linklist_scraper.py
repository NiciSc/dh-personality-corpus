import requests
import pandas as pd
import os

# this is for scraping the subcategories of fictional characters in every sorting

offset = 0
sortings = [
    "top",
    "new",
    "hot",
    "alphabet"
]

subcat_ids = [
    27, # superhero 27
    3,  # movie 3
    2,  # television 2 
    8,  # anime 8
    11, # gaming 11
    7,  # cartoons 7
    12, # literature 12 
    9,  # comics 9
    26, # webcomics 26
    13  # theatre 13
]

ids = []
url = "https://www.personality-database.com/profile/"

while (offset < 10500):

    # urls for requests, change sorting to new, top, hot, alphabetical for more variety
    # property id has to be 2 -> fictional character
    #response = requests.get(f"https://api.personality-database.com/api/v1/profiles?offset={offset}&limit=500&pid={subcat_ids}&sort={sorting}&property_id=2")
    for sorting in sortings:

        #for  subcat_id in subcat_ids:
        response = requests.get(f"https://api.personality-database.com/api/v1/profiles?offset={offset}&limit=500&cid=8&pid=2&sort={sorting}&cat_id=8&property_id=2")
    
        profiles = response.json()["profiles"]

        for profile in profiles:
            id = profile['id']
            ids.append(id)
                #print(id)
            #print(subcat_id)
        print(sorting)

    # größtes intervall das geht = 500
    offset += 500
    print(offset)



df = pd.DataFrame(ids)
output_path = "C:/Users/Harry/Documents/GitHub/dh-personality-corpus/links/ids_anime.csv"
df.to_csv(output_path, mode='a', header=not os.path.exists(output_path), index=False)