"""This module processes raw data in two ways:
    - make it publishable
    - make it easier to analyse"""
import json
import os

RAW_PATH = r'/PATH/TO/RAW/DATA'
EXTERNAL_PATH = r'/PATH/TO/EXTERNAL/FORMAT/DATA'
INTERNAL_PATH = r'/PATH/TO/INTERNAL/FORMAT/DATA'

with open('./resources/templates/internal_template.json', encoding='UTF-8') as file:
    internal_json_format = json.load(file)
with open('./resources/templates/corpus_template.json', encoding='UTF-8') as file:
    external_json_format = json.load(file)


def save_file(content, path):
    """Takes String and location to save as JSON"""
    formatted_json = open(rf'{path}', 'w', encoding='UTF-8')
    formatted_json.write(content)
    formatted_json.close()


count = 0
for root, dirs, files in os.walk(RAW_PATH):
    for file in files:
        if file.endswith(".json"):
            if (count % 10000) == 0:
                print(f"{count} done!")
            with open(rf'{root}/{file}', encoding='UTF-8') as json_file:
                raw_data = json.load(json_file)
            # Formats JSONs to fit external requirements
            external_json_dict = {}
            try:
                raw_data['topic_info']['topic'].pop('posts')
            except KeyError:
                pass
            for category in external_json_format:
                external_json_dict[category] = raw_data[category]
            external_json_string = json.dumps(external_json_dict)
            save_file(external_json_string,
                      rf'{EXTERNAL_PATH}/{file}')
            # Formats JSONs to fit internal requirements
            internal_json_dict = {}
            raw_data['breakdown_systems'] = raw_data['breakdown_systems']['1']
            raw_data['systems'] = raw_data['systems'][0]
            raw_data['vote_count_mbti'] = raw_data['systems']['system_vote_count']
            for category in internal_json_format:
                internal_json_dict[category] = raw_data[category]
            internal_json_string = json.dumps(internal_json_dict)
            save_file(internal_json_string,
                      rf'{INTERNAL_PATH}/{file}')
            count += 1

    print(rf'Finished {root}')
