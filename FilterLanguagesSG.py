from langdetect import detect
import json

def filter_english(json_list):
    filtered_list = []
    for j in json_list:
        try:
            if detect(j['conversations'][0]['value']) == 'en':
                filtered_list.append(j)
        except:
            print(j)
    return filtered_list

f = open('Datasets/sg_90k_part1.json')
sg_part1 = json.load(f)
f = open('Datasets/sg_90k_part2.json')
sg_part2 = json.load(f)
sg=sg_part1+sg_part2
sg_filtered=filter_english(sg)
with open("Datasets/sg_en.json", "w") as outfile:
    # write the dictionary to the file
    json.dump(sg_filtered, outfile)