"""This module processes raw data in two ways:
    - make it publishable
    - make it easier to analyse"""
import os
import json

with open('vong_template.json', encoding='UTF-8') as file:
    internal_json_format = json.load(file)
with open('corpus_template.json', encoding='UTF-8') as file:
    external_json_format = json.load(file)


def save_file(content, path):
    """Takes String and location to save as JSON"""
    formatted_json = open(rf'{path}', 'w', encoding='UTF-8')
    formatted_json.write(content)
    formatted_json.close()


for root, dirs, files in os.walk('profiles_subcat'):
    if dirs != []:
        for directory in dirs:
            try:
                os.mkdir(rf'externalCorpus/{directory}')
            except OSError as error:
                print(error)
            try:
                os.mkdir(rf'internalCorpus/{directory}')
            except OSError as error:
                print(error)
    for file in files:
        if file.endswith(".json"):
            with open(rf'{root}/{file}', encoding='UTF-8') as json_file:
                raw_data = json.load(json_file)
            # Formats JSONs to fit external requirements
            external_json_dict = {}
            try:
                for element in raw_data['topic_info']['topic']['posts']['posts']:
                    for key in ['username', 'user_pic_path', 'user_personality_type', 'is_mod']:
                        element.pop(key)
                        print("Popped!")
            except KeyError as error:
                print(f"Hier gibts wohl kein {error}")
            #print(raw_data)
            for category in external_json_format:
                external_json_dict[category] = raw_data[category]
            external_json_string = json.dumps(external_json_dict)
            save_file(external_json_string, rf'externalCorpus/{root.split("/")[1]}/{file}')
            # Formats JSONs to fit internal requirements
            internal_json_dict = {}
            raw_data['breakdown_systems'] = raw_data['breakdown_systems']['1']
            raw_data['systems'] = raw_data['systems'][0]
            for category in internal_json_format:
                internal_json_dict[category] = raw_data[category]
            internal_json_string = json.dumps(internal_json_dict)
            save_file(internal_json_string, rf'internalCorpus/{root.split("/")[1]}/{file}')

    print(rf'Finished {root}')
