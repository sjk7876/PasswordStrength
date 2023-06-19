import string

def main():
    # Password Rules
    #   No spaces
    #   At least 14 characters
    #   At least 2 uppercase
    #   At least 2 lowercase
    #   At least 2 symbols
    #   At least 2 numbers
    #   No dictionary words
    #   No common passwords
    
    # Start with 0 points
    # 10 = best
    # 7-9 = secure
    # 5-6 = moderate
    # 3-4 = weak
    # 0-2 = very weak
    
    score = 0
    length = 0
    uppers = 0
    lowers = 0
    symbol = 0
    number = 0
    
    # Grab input from stdin
    print("Enter the password to check here: ", end='')
    userPassword = input()
    
    if len(userPassword) > 1024:
        print("Password too long")
        return 0
    elif len(userPassword) >= 14:
        length = 1
      
    for letter in userPassword:
        if letter in string.punctuation and symbol < 2:
            symbol = symbol + 1
            continue
            
        if letter.isalpha:
            if letter.isdigit():
                if number < 2:
                    number = number + 1
                continue
            
            if letter.isupper():
                if uppers < 2:
                    uppers = uppers + 1
                continue
            
            if letter.islower():
                if lowers < 2:
                    lowers = lowers + 1
                continue
    
    score = length + uppers + lowers + symbol + number
        
    print("score:", score)
    print("length:", length)
    print("upper:", uppers)
    print("lower:", lowers)
    print("symbol:", symbol)
    print("number:", number)
    
    # print("Password:", userPassword)
    # print("Score:", score)


if (__name__ == "__main__"):
    main()
