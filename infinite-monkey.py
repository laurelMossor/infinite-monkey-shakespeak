# How long do you think it would take for a Python function to generate 
# just one sentence of Shakespeare? The sentence we’ll shoot for is: “methinks it is like a weasel”

#  The way we’ll simulate this is to write a function that generates a string that is 28 characters long 
# by choosing random letters from the 26 letters in the alphabet plus the space. 
# We’ll write another function that will score each generated string by comparing the randomly generated string to the goal.

# A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done. 
# If the letters are not correct then we will generate a whole new string.To make it easier to follow your program’s progress 
# this third function should print out the best string generated so far and its score every 1000 tries.

from random import choice

ALPHABET_SPACE = "abcdefghijklmnopqrstuvwxyz "

def alphabet_list(ALPHABET_SPACE):
    return list(ALPHABET_SPACE)

ALPHABET_LIST = alphabet_list(ALPHABET_SPACE)

def get_phrase():
    """Asks for user input string 
    and returns a length"""

    human_string = input("What phrase would you like the monkey to generate?\n>").lower()
    print(f"You put '{human_string}'... on it!")

    return len(human_string)

def generate_string(length):
    """Generate a string that is as long as intended phrase"""

    monkey_string = ""
    for i in range(length):
        monkey_string += choice(ALPHABET_LIST)
    
    print(monkey_string)

def MAIN():
    monkey_string_length = get_phrase()
    generate_string(monkey_string_length)


MAIN()