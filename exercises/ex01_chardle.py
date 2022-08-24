"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730575518"


five_character_word: str = input("Enter a 5-character word: ")
if len(five_character_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()


single_character: str = input("Enter a single character: ")
if len(single_character) != 1:
    print("Error: Character must be a single character.")
    exit()


instance_count: int = 0


print("Searching for " + single_character + " in " + five_character_word)


if five_character_word[0] == single_character:
    print(single_character + " found at index 0")
    instance_count = instance_count + 1

if five_character_word[1] == single_character:
    print(single_character + " found at index 1")
    instance_count = instance_count + 1

if five_character_word[2] == single_character:
    print(single_character + " found at index 2")
    instance_count = instance_count + 1

if five_character_word[3] == single_character:
    print(single_character + " found at index 3")
    instance_count = instance_count + 1

if five_character_word[4] == single_character:
    print(single_character + " found at index 4")
    instance_count = instance_count + 1

if instance_count == 0:
    print("No instances of " + single_character + " found in " + five_character_word)
else:
    print(str(instance_count) + " instances of " + single_character + " found in " + five_character_word)