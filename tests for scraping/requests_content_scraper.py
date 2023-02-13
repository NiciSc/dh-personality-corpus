import requests
import json
import csv


with open('id_list.csv', 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader: 
        
        id = row[0].split('/')[-1]
        response = requests.get(f"https://api.personality-database.com/api/v1/profile/{id}") 
        if (
            response.status_code != 204 and
            response.headers["content-type"].strip().startswith("application/json")
        ):
            try:
                content_char = response.json()
            except ValueError:
                print("error")
        # decide how to handle a server that's misbehaving to this extent
        
            

        with open(f'profiles/character_id_{id}.json', 'w') as f:
            json.dump(content_char, f)