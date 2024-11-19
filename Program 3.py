# Owen O'Neil
# Program 3: Palindrome Checker
# CSC 201-2
# 10/4/24


# import deque from class
from CSC201UT import Deque
# import regular expressions method
import re

# subroutine that check if a phrase is a palindrome
def is_palindrome(phrase):
    # set deque class from import
    deque = Deque()
    # gets rid of everything that is not a letter
    # https://builtin.com/software-engineering-perspectives/python-remove-character-from-string
    # site introduced me to "re.sub" which is a builtin function that removes all non letter characters
    # more efficient than going through a list of characters and determining what is and isn't a letter
    phrase_lower = phrase.lower()
    phrase_lower = re.sub(r'[^a-zA-Z]', '', phrase_lower)

    # add the letters from the phrase into to a que
    for letter in phrase_lower:
        deque.add_front(letter)

    # keeps running as long as the phrase is greater than 1 letter
    while deque.size() > 2:
        # remove the front and rear of the que, if they are not the same, return false
        if deque.remove_front() != deque.remove_rear():
            return False
        # if the que is empty, return true
        if deque.is_empty():
            return True
    # if no false conditions are met return true
    return True


# open the file containing the phrases
phrases_list = ("phrases-1.txt")
with (open(phrases_list, "r")) as f:
    # read all the lines in the file
    phrases = f.readlines()
    # for a phrase in the phrase list, check if it is a palindrome using the subroutine
    for phrase in phrases:
        # if it is a palindrome, return the original phrase
        if is_palindrome(phrase):
            print(phrase)


















