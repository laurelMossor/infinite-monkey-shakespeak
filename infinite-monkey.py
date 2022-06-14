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
    Returns the string and its length"""

    human_string = input("What phrase would you like the monkey to generate?\n>").lower()
    print(f"You put '{human_string}'... on it!")

    return human_string

def generate_string(human_string):
    """Generate a string that is as long as intended phrase"""

    monkey_string = ""
    for i in range(len(human_string)):
        monkey_string += choice(ALPHABET_LIST)
    
    # print(monkey_string)
    return monkey_string

def score_monkey_string(monkey_string, human_string):
    """Takes in the human string and compares it to the monkey/generated string
    Returns a score out of 100"""

    # Compare each index to each other and if the same, increase counter

    correct = 0
    out_of = len(human_string)

    for i in range(len(human_string)):
        if monkey_string[i] == human_string[i]:
            correct += 1

    monkey_score = (correct/out_of)*100

    # print(monkey_score)
    return monkey_score

def dance_monkey(human_string):
    """Repeatedly call generate and score, then if 100% of the letters are correct we are done. 
    If the letters are not correct then we will generate a whole new string. 
    Print out the best string generated so far and its score every 1000 tries."""

    num_attempts = 0
    best_match_yet = generate_string(human_string)
    best_score_yet = score_monkey_string(best_match_yet, human_string)

    while best_score_yet != 100:

        num_attempts += 1
        monkey_string = generate_string(human_string)
        score = score_monkey_string(monkey_string, human_string)

        if score > best_score_yet:
            best_score_yet = score
            best_match_yet = monkey_string

        if num_attempts % 1000 == 0:
            print(num_attempts)
            print(best_score_yet)
            print(best_match_yet)
    
    print(f"WOO HOO! After {num_attempts}, the monkey generated {best_match_yet}")



def MAIN():
    human_string = get_phrase()
    dance_monkey(human_string)


MAIN()