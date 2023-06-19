import string
import argparse

ASCII_ART = "\
--------------------------------------------------------------------------\n\
\t\t      _                        _   _     \n\
\t\t     | |                      | | | |    \n\
\t\t  ___| |_ _ __ ___ _ __   __ _| |_| |__  \n\
\t\t / __| __| '__/ _ \ '_ \ / _` | __| '_ \ \n\
\t\t \__ \ |_| | |  __/ | | | (_| | |_| | | |\n\
\t\t |___/\__|_|  \___|_| |_|\__, |\__|_| |_|\n\
\t\t                          __/ |          \n\
\t\t                         |___/           \n\
--------------------------------------------------------------------------"



# Global Password Strength Requirements
NUM_UPPER = 2
NUM_LOWER = 2
NUM_NUMBERS = 2 
NUM_SYMBOLS = 2
NUM_CHARACTERS = 14


def checkStrength(userPassword, commonPasswords, commonWords):
    # Default Password Rules
    #   No spaces
    #   At least 14 characters
    #   At least 2 uppercase
    #   At least 2 lowercase
    #   At least 2 symbols
    #   At least 2 numbers
    #   No dictionary words
    #   No common passwords
    #   Max Length 1024 characters
    
    # Start with 0 points
    # 9   = best
    # 7-8 = secure
    # 5-6 = moderate
    # 3-4 = weak
    # 0-2 = very weak
    
    score = 0
    length = 0
    uppers = 0
    lowers = 0
    symbol = 0
    number = 0
    
    answer = commonPasswords.find(userPassword)
    if answer != -1:
        print("Password found in list of most common passwords")
        return 0
        
    answer = 0
    
    answer = commonWords.find(userPassword)
    if answer != -1:
        print("Password found in list of common words")
        return -1
        
    
    if len(userPassword) > 1024:
        print("Password too long")
        return -1
    
    elif len(userPassword) >= 14:
        length = 1
      
    for letter in userPassword:
        if letter in string.punctuation and symbol < NUM_SYMBOLS:
            symbol = symbol + 1
            continue
            
        if letter.isalpha:
            if letter.isdigit():
                if number < NUM_NUMBERS:
                    number = number + 1
                continue
            
            if letter.isupper():
                if uppers < NUM_UPPER:
                    uppers = uppers + 1
                continue
            
            if letter.islower():
                if lowers < NUM_LOWER:
                    lowers = lowers + 1
                continue
    
    score = length + uppers + lowers + symbol + number
    
    return score
        
    # print("score:", score)
    # print("length:", length)
    # print("upper:", uppers)
    # print("lower:", lowers)
    # print("symbol:", symbol)
    # print("number:", number)


def main():
    parser = argparse.ArgumentParser(description="Checks the strength of a given list of passwords",
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)    
    parser.add_argument("-i", "--input_file", default="stdin", help="location of the input file")
    parser.add_argument("-o", "--output_file", default="stdout", help="location of the output file")
    parser.add_argument("-v", "--verbosity", default="2", type=int, choices=range(1,4), help="how detailed the output should be (1-3)")
    args = vars(parser.parse_args())
    
    passwordList = []
    
    # Input Arguments
    inputFile = args["input_file"]
    outputFile = args["output_file"]
    verbosity = args["verbosity"]
    
    # Print fancy jazz
    print(ASCII_ART)
            
    # Grab input from stdin
    
    print("Enter in a newline separated list of passwords, ending with a blank line:")
    while True:
        password = input()
        
        if password == "":
            break
            
        passwordList.append(password)
    
    f = open("100k_password.txt", "r", encoding="utf-8")
    commonPasswords = f.read()
    
    f = open("10k_words.txt", "r", encoding="utf-8")
    commonWords = f.read()
    
    for p in passwordList:
        print("Password:", p)
        print("Score:", checkStrength(p, commonPasswords, commonWords))
        print()
        


if (__name__ == "__main__"):
    main()
