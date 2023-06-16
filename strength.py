SYMBOLS_LIST = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"


def main():
    # Grab input from stdin
    print("Enter the password to check here: ", end='')
    userPassword = input()
    
    # Password Rules
    #   No spaces
    #   At least 14 characters
    #   At least 2 uppercase
    #   At least 2 lowercase
    #   At least 2 symbols
    #   At least 2 numbers
    #   No dictionary words
    #   No common passwords
    
    score = 0
    maxScore = 9
    
    for letter in userPassword:
        print("e")
        
    
    print(userPassword)


if (__name__ == "__main__"):
    main()
