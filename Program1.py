
######################################
# Random Writer programming assignment
# Owen O'Neil
# 8/29/24
######################################

# import libraries
from random import randint
import random

###########
# FUNCTIONS
###########
# returns a random seed of length level (or k) from the book
def get_seed():
    start_index = randint(0, len(text) - k)
    # get the starting index
    seed = text[start_index:start_index + k]
    # the seed is the starting index + k
    return seed

# returns a random next character given a seed from the book
def get_next_char(seed):
    # initialize the list of characters
    following_character = []
    find_index = 0
    # initialize the current index (where we begin to look in the book)
    while (text.lower().find(seed.lower(), find_index)) != -1:
        # convert the book and the seed to lowercase and abort if the seed is not found (or it's at the end of the book)
        find_index = text.lower().find(seed.lower(), find_index)
        # find the index of the seed in the book beginning at the current index
        # continually find the seed in the book
        if find_index + k < len(text):
            # if the seed index plus the level is less than the length of the text than the program will run
            character = text[find_index + k]
            # find the next character after the seed
            following_character.append(character)
            # add the characters after the seed in the book and put it in the array
        find_index += 1
        # get teh next index


    if len(following_character) == 0:
        return None
    # if there is no following characters than the program will return none and find a new seed

    return random.choice(following_character)
    # if there is at least one next character in the list of characters, return a randomly chosen one


######
# MAIN
######
book = ("hg-wells_the-time-machine.txt")\
# the sample text
k = 25
# length of the seed
length = 150
# characters used in a section from the book
# grab the book
with open(book, "r") as f:
    text = f.read()
    # reads the text
    text = text.replace("\n", " ")
    # overwrites text and puts it on one line

seed = get_seed()
# set a variable to the seed subroutine

final_text = ""
# make the final text a string
final_text += seed
# add the seed to the start of the final text
i = 0
while i <= length:
    # repeat as long as there isn't enough output yet
    next_char = get_next_char(seed)
    # set a variable to the next character subroutine

    if next_char == None:
        # if the next character doesn't exist, get a new seed
        seed = get_seed()
        final_text += seed
        # add the new seed to the final text

    else:
        # get a random next character
        final_text += next_char
        # add the next character to the final text
        seed = seed[1:] + next_char
        # move the seed over by 1 so get_character can read the correct amount of characters while also using the new characters
        i += 1
        # increment the distance between the length of the book by 1
print(final_text)
# display the output





