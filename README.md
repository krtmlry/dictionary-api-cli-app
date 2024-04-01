# Dictionary CLI app

## About
This is the updated version of my previous dictionary cli app. The old cli app only returns the first available meaning. This new version can return all meanings which are grouped by according to its part of speech function.

The old version of the this code can be seen here:
> link: https://github.com/krtmlry/PY4E/tree/254801f58bb98be47e04118d9ac7aa99b27735df/dictionary_api
---
## Major changes
### 1. User input data validation
A. Proper use of try-except block replaced if-else statements that are functioning well but does not fit the given scenario. The previous code did not validate data on the user level but instead, it just sends the request(url+input) to the api and lets the api to validate the request.

**Old version data validation**
```
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
```
>The code above accepts any user invalid input such as:
`123`,`123.123`, `Hello123`, `he llo`, `he llo122`.
It will return the `word` variable containing the user input and will be passed down to the function below.

**API Request**
```
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
```
> The code above will send the request to the API without input validation. Input validation must be handled in the user level to avoid unnecessary API requests.

**New version data validation**
```
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
```
> This new approach will now validate the user input before it passes it to `process_input()` function to send the API request.

## App functions demo

### User enters a valid word
![new-main-flow](https://github.com/krtmlry/dictionary-api-cli-app/blob/main/img/new-main-flow.png)
> User enters the word "Hello" and all availabe definitions are displayed.

### New data validation
![new-data-validation](https://github.com/krtmlry/dictionary-api-cli-app/blob/main/img/new-datavalidation.png)
> The new data validation works by using the `isaplha()` method, which will only return `True` if the user input only contains alphabet letters from (a-z)

