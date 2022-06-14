# How long do you think it would take for a Python function to generate 
# just one sentence of Shakespeare? The sentence we’ll shoot for is: “methinks it is like a weasel”

#  The way we’ll simulate this is to write a function that generates a string that is 28 characters long 
# by choosing random letters from the 26 letters in the alphabet plus the space. 
# We’ll write another function that will score each generated string by comparing the randomly generated string to the goal.

# A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done. 
# If the letters are not correct then we will generate a whole new string.To make it easier to follow your program’s progress 
# this third function should print out the best string generated so far and its score every 1000 tries.


def get_phrase():
    """Asks for user input string and returns a length"""
    monkey_string = input("What phrase would you like the monkey to generate?\n>").lower()
    print(f"You put '{monkey_string}'... on it!")
    return len(monkey_string)


def generate_string(input):
    """Generate a string that is as long as intended phrase"""
    print(input)

def MAIN():
    generate_string(get_phrase())


MAIN()