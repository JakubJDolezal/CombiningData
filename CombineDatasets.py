import json
from datasets import load_dataset
gpt4all = load_dataset("nomic-ai/gpt4all-j-prompt-generations", revision="v1.2-jazzy")
f = open('Datasets/databricks-dolly-15k.jsonl')
import pandas as pd
jsonObj = pd.read_json(path_or_buf=f, lines=True)
f = open('Datasets/alpaca_data.json', )
alpaca = json.load(f)
f = open('Datasets/sg_en_formatted_shortened.json', )
sg_part = json.load(f)
def convert_databricks(data):
    for item in data:
        item["input"] = item.pop("context")
        item['source']='databricks'
        item["output"] = item.pop("response")
    return data
databricks=convert_databricks(jsonObj.to_dict('records'))
print('databricks')
gpt4all=gpt4all.to_dict()
gpt4all["instruction"]=gpt4all.pop("prompt")
gpt4all["output"]=gpt4all.pop("response")

print('gpt4all')
gpt4all_mod=[]
for i in range(len(gpt4all['source'])):
    new_dict = {}
    # iterate through the keys of the original dict
    for key in gpt4all.keys():
        new_dict[key] = gpt4all[key][i]
    new_dict["input"]= ""
    gpt4all_mod.append(new_dict)

total=databricks+alpaca+gpt4all_mod

def add_user_assistant(data):
    for item in data:
        item["input"] = 'User: '+item["input"]+' Assistant:'


def add_blank_input(data):
    for item in data:
        item["input"] = ""
        item["source"] = "sharegpt"
    return data

sg_part=add_blank_input(sg_part)
total = total+sg_part
with open("Datasets/total.json", "w") as outfile:
    # write the dictionary to the file
        json.dump(total, outfile)