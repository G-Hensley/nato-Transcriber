import pandas

# Read the CSV file
alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary from the CSV data
dict_alphabet = {row.letter: row.code for (index, row) in alphabet_df.iterrows()}

# Define the function to generate the phonetic list
def generate_phonetic():
    user_word = input("What word would you like transcribed? ").upper()

    # Try to generate the phonetic list
    try:
        phonetic_list = [dict_alphabet[letter] for letter in user_word]
    # If the user enters a letter that is not in the dictionary, print an error message
    except KeyError:
        print("Please enter a letter.")
        # Call the function again to ask for a new word
        generate_phonetic()
    else:
        print(phonetic_list)

generate_phonetic()
