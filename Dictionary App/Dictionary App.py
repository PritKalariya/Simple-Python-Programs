import json
from difflib import get_close_matches

# Loading data
# Dict type
data = json.load(open("data.json"))

# Returning the definition of the word
# Main program logic
def meaning(word):
    word = word.lower()

    if word in data:
        return data[word]

    elif word.title() in data:
        return data[word.title()]

    elif word.upper() in data:
        return data[word.upper()]

    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean \"%s\" instead ? Press Y for yes, or N for no: " % get_close_matches(word, data.keys())[0])

        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "No such word! Please double check it :)"
        else:
            return "We didn't understand your query."

    else:
        return "No such word! Please double check it :)"

# Main user input
word = input("Enter word: ")

# Storing the output in a variable for formatting
output = meaning(word)

# Output formatting
if type(output) == list:
    for item in output:
        print(f"-> {item}")
else:
    print(output)