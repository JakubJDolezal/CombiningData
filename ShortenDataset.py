from transformers import AutoTokenizer, LlamaTokenizer
import json

f = open('Datasets/sg_en_formatted.json', )
sg = json.load(f)
tokenizer = LlamaTokenizer.from_pretrained(r'C:\Users\jakub\Downloads\VicunaModel')

def shorten_text(text, desired_length):
    # Load tokenizer

    # Tokenize the text

    # Shorten the beginning of the text to approximately the desired length in terms of number of tokens
    if len(text) > desired_length:
        num_tokens_to_remove = len(text) - desired_length
        shortened_text = text[num_tokens_to_remove:]
    else:
        shortened_text = text

    return shortened_text
print(len(sg))
for i in range(len(sg)):
    sg[i]['instruction'] = shorten_text(sg[i]['instruction'], 3000)
    print(i)

with open("Datasets/sg_en_formatted_shortened.json", "w") as outfile:
    # write the dictionary to the file
        json.dump(sg, outfile)
