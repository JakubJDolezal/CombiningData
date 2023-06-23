import json


f = open('Datasets/sg_en_MarkDown.json', )
sg_part = json.load(f)


def format_conversations(conversations):
    output = []
    k = 0
    for item in conversations:
        conversation = item['conversations']
        for i in range(1, int(len(conversation) / 2)):
            output.append({"instruction": "", "input": "", "output": ""})
            for j in range(0, i):
                if j != i - 1:
                    if conversation[2*j]['from'] == 'human':
                        output[k]['instruction'] += "Human:" + conversation[2*j]['value'] + " Assistant: "
                    if conversation[2*j+1]['from'] == 'gpt':
                        output[k]['instruction'] += conversation[2*j+1]['value']

                else:
                    if conversation[2*j]['from'] == 'human':
                        output[k]['instruction'] += "Human:" + conversation[2*j]['value'] + " Assistant: "
                    if conversation[2*j+1]['from'] == 'gpt':
                        output[k]['output'] += conversation[2*j+1]['value']
            k = k + 1
            print(k)

    return output


sg_formatted = format_conversations(sg_part)

with open("Datasets/sg_en_formatted.json", "w") as outfile:
    # write the dictionary to the file
    json.dump(sg_formatted, outfile)