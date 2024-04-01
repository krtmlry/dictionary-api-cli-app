import json
import requests

def get_word():
    while True:
        word = input('\nEnter word (type yy to exit): ').lower()
        if word == 'yy':
            print('Exiting program...')
            break
        elif len(word) == 0:
            print('Please type a word.')
        else:
            return word

def get_url(word):
    url = 'https://api.dictionaryapi.dev/api/v2/entries/en/' + word
    req = requests.get(url)
    data = json.loads(req.text) #convert to python object text
    
    #check data type of json response: dict {} for error, list [] for valid
    if isinstance(data, dict):
        print(f"Apologies, the word '{word}' is not available in our system.\n")
        return None

    if isinstance(data, list):
        get_def = data[0]['meanings'][0]['definitions'][0]['definition']
        return get_def

def print_output(word, get_def):
    print(f"'{word.capitalize()}' - {get_def}\n")    

def valid_action():
    while True:
        action = input('Enter a new word? y/n: ').upper()
        if action == 'Y' or action == 'N':
            return action == 'Y'
        else:
            print('Invalid input. Only Y or N is accepted.\n')

def main():
    print("\nSimple dictionary using dictionaryapi.dev")
    while True:
        word = get_word()
        if word is None: #check if the return value from get_word() is None(for yy) or valid
            break
        
        get_def = get_url(word)
        if get_def is not None:
            print_output(word, get_def)
        
        if not valid_action(): # valid_action = return('Y')
            print('Exiting program...')
            break

if __name__ == '__main__':
    main()