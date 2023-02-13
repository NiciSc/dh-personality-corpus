"""This module processes raw data in two ways:
    - make it publishable
    - make it easier to analyse"""
import json
import os

with open('vong_template.json', encoding='UTF-8') as file:
    internal_json_format = json.load(file)


def save_file(content, path):
    """Takes String and location to save as JSON"""
    formatted_json = open(rf'{path}', 'w', encoding='UTF-8')
    formatted_json.write(content)
    formatted_json.close()


count = 0
for root, dirs, files in os.walk('../internalCorpus'):
    for file in files:
        if file.endswith(".json"):
            # if count == 5:
            #    break
            if count % 100 == 0 and count > 0:
                print('100 files processed')
            with open(rf'{root}/{file}', encoding='UTF-8') as json_file:
                raw_data = json.load(json_file)
            # Formats JSONs to fit internal requirements
            internal_json_dict = {}
            raw_data['vote_count_mbti'] = raw_data['systems']['system_vote_count']
            for category in internal_json_format:
                internal_json_dict[category] = raw_data[category]
            internal_json_string = json.dumps(internal_json_dict)
            save_file(internal_json_string, rf'../vongNeu/{file}')
            count += 1
