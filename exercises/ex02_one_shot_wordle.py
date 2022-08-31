"""This is a one-shot wordle"""

__author__ = "730575518"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret_word: str = "python"
user_input: str = input("What is your 6-letter guess? ")
index: int = 0
string_indicator: str = ""


while len(user_input) != len(secret_word):
    user_input = input("That was not 6 letters! Try again: ")

while index < len(secret_word):
    if user_input[index] == secret_word[index]:
        string_indicator = string_indicator + GREEN_BOX
    else:
        alternate_index: int = 0
        character_exists: bool = False

        while character_exists != True and alternate_index < len(secret_word):
            if user_input[index] == secret_word[alternate_index]:
                character_exists = True
            else:
                alternate_index = alternate_index + 1
        
        if character_exists:
            string_indicator = string_indicator + YELLOW_BOX
        else:
            string_indicator = string_indicator + WHITE_BOX
            
    index = index + 1

print(string_indicator)

if user_input == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")