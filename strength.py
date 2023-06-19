import string
import argparse
import sys


ASCII_ART = "\
|--------------------------------------------------------------------------|\n\
|\t\t      _                        _   _     \t\t   |\n\
|\t\t     | |                      | | | |    \t\t   |\n\
|\t\t  ___| |_ _ __ ___ _ __   __ _| |_| |__  \t\t   |\n\
|\t\t / __| __| '__/ _ \ '_ \ / _` | __| '_ \ \t\t   |\n\
|\t\t \__ \ |_| | |  __/ | | | (_| | |_| | | |\t\t   |\n\
|\t\t |___/\__|_|  \___|_| |_|\__, |\__|_| |_|\t\t   |\n\
|\t\t                          __/ |          \t\t   |\n\
|\t\t                         |___/           \t\t   |\n\
|--------------------------------------------------------------------------|"


# Global Password Strength Requirements
NUM_UPPER = 2
NUM_LOWER = 2
NUM_NUMBERS = 2 
NUM_SYMBOLS = 2
NUM_CHARACTERS = 14

# Default Password Rules
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


class Password:
    def __init__(self, password):
        self.password = password
        self.score = 0
        self.length = 0
        self.uppers = 0
        self.lowers = 0
        self.symbol = 0
        self.number = 0
        self.note = ""
        self.strength = ""
        
    def update(self, commonPasswords, commonWords):
        answer = commonPasswords.find(self.password)
        if answer != -1:
            self.note = "Password found in list of most common passwords"
            self.score = -1
            
        answer = 0
        
        answer = commonWords.find(self.password)
        if answer != -1:
            self.note = "Password found in list of common words"
            self.score = -1
            
        
        if len(self.password) > 1024:
            self.note = "Password too long"
            self.score = -1
        
        if self.score != -1:
            if len(self.password) >= 14:
                self.length = 1
            
            for letter in self.password:
                if letter in string.punctuation and p.symbol < NUM_SYMBOLS:
                    self.symbol = self.symbol + 1
                    continue
                    
                if letter.isalpha:
                    if letter.isdigit():
                        if self.number < NUM_NUMBERS:
                            self.number = self.number + 1
                        continue
                    
                    if letter.isupper():
                        if self.uppers < NUM_UPPER:
                            self.uppers = self.uppers + 1
                        continue
                    
                    if letter.islower():
                        if self.lowers < NUM_LOWER:
                            self.lowers = self.lowers + 1
                        continue
            
            self.score = self.length + self.uppers + self.lowers + self.symbol + self.number
            
            if 0 <= self.score <= 2:
                self.strength = "Very Weak"
            elif 3 <= self.score <= 4:
                self.strength = "Weak"
            elif 5 <= self.score <= 6:
                self.strength = "Moderate"
            elif 7 <= self.score <= 8:
                self.strength = "Secure"
            elif self.score == 9:
                self.strength = "Very Secure"


def checkStrength(p, commonPasswords, commonWords):
    answer = commonPasswords.find(p.password)
    if answer != -1:
        p.note = "Password found in list of most common passwords"
        return -1
        
    answer = 0
    
    answer = commonWords.find(p.password)
    if answer != -1:
        p.note = "Password found in list of common words"
        return -1
        
    
    if len(p.password) > 1024:
        p.note = "Password too long"
        return -1
    
    elif len(p.password) >= 14:
        p.length = 1
      
    for letter in p.password:
        if letter in string.punctuation and p.symbol < NUM_SYMBOLS:
            p.symbol = p.symbol + 1
            continue
            
        if letter.isalpha:
            if letter.isdigit():
                if p.number < NUM_NUMBERS:
                    p.number = p.number + 1
                continue
            
            if letter.isupper():
                if p.uppers < NUM_UPPER:
                    p.uppers = p.uppers + 1
                continue
            
            if letter.islower():
                if p.lowers < NUM_LOWER:
                    p.lowers = p.lowers + 1
                continue
    
    p.score = p.length + p.uppers + p.lowers + p.symbol + p.number
            
    # print("score:", score)
    # print("length:", length)
    # print("upper:", uppers)
    # print("lower:", lowers)
    # print("symbol:", symbol)
    # print("number:", number)


def main():
    parser = argparse.ArgumentParser(description="Checks the strength of a given list of passwords",
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)    
    parser.add_argument("-i", "--input_file", help="location of the input file")
    parser.add_argument("-o", "--output_file", default="stdout", help="location of the output file")
    parser.add_argument("-v", "--verbosity", default="2", type=int, choices=range(1,4), help="how detailed the output should be (1-3)")
    args = vars(parser.parse_args())
    
    passwordList = []
    
    # Input Arguments
    inputFile = args["input_file"]
    outputFile = args["output_file"]
    verbosity = args["verbosity"]
        
    # Check if input file exists
    if inputFile != None:
        try:
            inTest = open(inputFile, "r")
            inTest.close()
                
        except FileNotFoundError:
            print("File", inputFile, "not found")
            return 0
    
    # # Check if output file exists
    # if outputFile != "stdout":
    #     try:
    #         f = open(outputFile, "r")
                
    #     except FileNotFoundError:
    #         print("File", outputFile, "not found")
    #         return 0
    
    # Print fancy jazz
    print(ASCII_ART)
    
    # Open files for future checks
    passF = open("100k_password.txt", "r", encoding="utf-8")
    commonPasswords = passF.read()
    passF.close()
    
    wordF = open("10k_words.txt", "r", encoding="utf-8")
    commonWords = wordF.read()
    wordF.close()

    # Grab passwords from given location
    # if inputFile == "stdin":
    #     print("Enter in a newline separated list of passwords, ending with a blank line:")
    #     while True:
    #         t = input()
            
    #         if t == "":
    #             break
            
    #         temp = Password("")
    #         temp.password = t.rstrip()
            
    #         checkStrength(temp, commonPasswords, commonWords)  
            
    #         passwordList.append(temp)
    
    # else:
    #     try:
    #         inF = open(inputFile, "r")
    #         inputLines = inF.readlines()
            
    #         for line in inputLines:
    #             temp = Password("")
    #             temp.password = line.rstrip()
                
    #             checkStrength(temp, commonPasswords, commonWords)  
                
    #             passwordList.append(temp)
            
    #         inF.close()
            
    #     except:
    #         print("Error reading input file -", inputFile)
            
    try:
            if inputFile == None:
                inF = sys.stdin
            else:
                inF = open(inputFile, "r")
            
            line = inF.readline()
            
            while line != "":
                temp = Password("")                
                temp.password = line.rstrip()
                                
                if temp.password == "":
                    break;
                                
                temp.update(commonPasswords, commonWords)  
                # checkStrength(temp, commonPasswords, commonWords)  
                                
                passwordList.append(temp)
                
                line = inF.readline()
            
            inF.close()
            
    except Exception as error: 
            print(error)
    # except: 
    #         print("Error reading input file -", inputFile)
    
    for p in passwordList:
        print(p.password, p.score)
    
    return 0
    
    if outputFile == "stdout":
        for p in passwordList:
            # checkStrength(p, commonPasswords, commonWords)
            
            print("Password:", p.password, end="\t")
            print("Score:", p.score)
            print()
    
    else:
        try:
            outF = open(outputFile, "w")
            
            lines = []
            
            for p in passwordList:
                # checkStrength(p, commonPasswords, commonWords)                
                lines.append("Password: " + p.password + "\tScore:" + str(p.score) + "\n")
                            
            outF.writelines(lines)
            outF.close()
            
            print("Written to file -", outputFile)
            
        except:
            print("Error writing to output file -", outputFile)


if (__name__ == "__main__"):
    main()
