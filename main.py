import requests
import string
import json

def get_input():
    while True:
        try:
            print("\nDictionary CLI app")
            print("\n*** Type 'YY' to exit. ***")
            word = input("Enter a word: ").upper()
            if not word.isalpha():
                raise ValueError("ERROR: Empty characters, words with spaces and numbers are not allowed.\n")
            else:
                return word
        except ValueError as e:
            print(e)

def process_input(word):
    url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'
    res = requests.get(url+word)
    while True:
        if word == 'YY':
            print('Exiting program...\n')
            break
        else:
            return res

def get_word(res):
    json_data = json.loads(res.text)
    if isinstance(json_data, dict):
        print("Sorry, this word is not available in our dictionary.")
        return None
    if isinstance(json_data, list):
        return json_data

def parse_json(json_data):
    data_list = []
    for item in json_data:
        for meaning in item['meanings']:
            part_of_speech = meaning['partOfSpeech']
            for definition in meaning['definitions']:
                word_def = definition['definition']
                data_pair = [part_of_speech, word_def]
                data_list.append(data_pair)
    return data_list

def data_catalog(data_list):
    data_cat = {}    
    for item in data_list:
        key = item[0]
        value = item[1]
        if key in data_cat:
            data_cat[key].append(value)
        else:
            data_cat[key] = [value]
    return data_cat

def display_meanings(data_cat,word):
    word = word.casefold().capitalize()
    print(f"\nDefinitions for '{word}':")
    for key,values in data_cat.items():
        print(f"\n'{word}' ({key})")
        for item in values:
            idx = values.index(item)
            print(f"{idx+1}. {item}")

def main():
    while True:
        word = get_input()
        res = process_input(word)
        if res is None:
            break
        
        json_data = get_word(res)
        if json_data is not None:
            data_list = parse_json(json_data)
            data_cat = data_catalog(data_list)
            display_meanings(data_cat,word)


if __name__ == '__main__':
    main()