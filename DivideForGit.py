import json

f = open('LLamaFinetuningDataCombined/Datasets/total.json', )
total = json.load(f)
with open("LLamaFinetuningDataCombined/Datasets/total1.json", "w") as outfile:
    # write the dictionary to the file
    json.dump(total[:int(len(total) / 2)], outfile)
with open("LLamaFinetuningDataCombined/Datasets/total2.json", "w") as outfile:
    # write the dictionary to the file
    json.dump(total[int(len(total) / 2):], outfile)
