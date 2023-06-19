import string
import argparse
import sys


ASCII_ART1 = '''
|--------------------------------------------------------------------------|\n
|\t\t      _                        _   _     \t\t   |\n
|\t\t     | |                      | | | |    \t\t   |\n
|\t\t  ___| |_ _ __ ___ _ __   __ _| |_| |__  \t\t   |\n
|\t\t / __| __| '__/ _ \ '_ \ / _` | __| '_ \ \t\t   |\n
|\t\t \__ \ |_| | |  __/ | | | (_| | |_| | | |\t\t   |\n
|\t\t |___/\__|_|  \___|_| |_|\__, |\__|_| |_|\t\t   |\n
|\t\t                          __/ |          \t\t   |\n
|\t\t                         |___/           \t\t   |\n
|--------------------------------------------------------------------------|'''

ASCII_ART = '''\
|-------------------------------------------------------------------------|
|\t___  ____ ____ ____ _ _ _ ____ ____ ___     ___ _ _  _ ____ \t  |
|\t|__] |__| [__  [__  | | | |  | |__/ |  \     |  | |\/| |___ \t  |
|\t|    |  | ___] ___] |_|_| |__| |  \ |__/     |  | |  | |___ \t  |
|-------------------------------------------------------------------------|\n'''



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
        self.strength = ""
        
    def update(self, commonPasswords, commonWords):
        answer = commonPasswords.find(self.password)
        if answer != -1:
            self.strength = "Common Pass"
            self.score = -1
            
        answer = 0
        
        answer = commonWords.find(self.password)
        if answer != -1:
            self.strength = "Common Word"
            self.score = -1
            
        
        if len(self.password) > 1024:
            self.strength = "Too long"
            self.score = -1
        
        if self.score == -1:
            self.score = 0
        else:
            if len(self.password) >= 14:
                self.length = 1
            
            for letter in self.password:
                if letter in string.punctuation and self.symbol < NUM_SYMBOLS:
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
                self.strength = "Very Weak  "
            elif 3 <= self.score <= 4:
                self.strength = "Weak       "
            elif 5 <= self.score <= 6:
                self.strength = "Moderate   "
            elif 7 <= self.score <= 8:
                self.strength = "Secure     "
            elif self.score == 9:
                self.strength = "Very Secure"


def main():
    # Handle parameters
    parser = argparse.ArgumentParser(description="Checks the strength of a given list of passwords",
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)    
    parser.add_argument("-i", "--input_file", help="location of the input file")
    parser.add_argument("-o", "--output_file", help="location of the output file")
    parser.add_argument("-v", "--verbosity", default="2", type=int, choices=range(1,4), help="how detailed the output should be (1-3)")
    args = vars(parser.parse_args())
    
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
    
    # Print fancy jazz
    if inputFile == None or outputFile == None:
        print(ASCII_ART)
    
    # Open files for future checks
    passF = open("100k_password.txt", "r", encoding="utf-8")
    commonPasswords = passF.read()
    passF.close()
    
    wordF = open("10k_words.txt", "r", encoding="utf-8")
    commonWords = wordF.read()
    wordF.close()
    
    passwordList = []

    # Grab passwords from given location
    try:
        if inputFile == None:
            print("> Enter a list of passwords, with with each password on its own line and\n> an empty line to finish.")
            inF = sys.stdin
        else:
            inF = open(inputFile, "r")
                
        line = inF.readline()
                
        while line != "":
            temp = Password("")                
            temp.password = line.rstrip()
                                    
            if temp.password == "":
                break
                                    
            temp.update(commonPasswords, commonWords)  
                                                    
            passwordList.append(temp)
                    
            line = inF.readline()
                
        inF.close()
                
    # except Exception as error: 
    #         print(error)
    except: 
        print("Error reading input file -", inputFile)
    
    # for p in passwordList:
    #     print(p.password, p.score)
    
    # return 0
    
    try:
        if outputFile == None:
            outF = sys.stdout
        else:
            outF = open(outputFile, "w")
        
        if verbosity == 1:
            outF.write("Strength\tPassword\n")
            outF.write("------------------------\n")
            
            for p in passwordList:
                outF.write(p.strength + "\t" + p.password + "\n")
                            
        
            
                
        elif verbosity == 2:
            outF.write("Score (Max 9)\tStrength\tPassword\n")
            outF.write("----------------------------------------\n")
            
            for p in passwordList:
                outF.write(str(p.score) + "\t\t" + p.strength + "\t" + p.password + "\n")
                
        else:
            outF.write("Length\t# Uppercase\t# Lowercase\t# Symbols\t# Numbers\tScore (Max 9)\tStrength\tPassword\n")
            outF.write("----------------------------------------------------------------------------------------------------------------\n")
            
            for p in passwordList:
                outF.write(str(p.length) + "\t" + str(p.uppers) + "\t\t" + \
                    str(p.lowers) + "\t\t" + str(p.symbol) + "\t\t" + str(p.number) + "\t\t" + \
                    str(p.score) + "\t\t" + p.strength + "\t" + p.password + "\n")
                                        
        outF.close()
            
        if outputFile != None:
            print("Written to file -", outputFile)
            
    except Exception as error: 
            print(error)
    # except:
    #     print("Error writing to output file -", outputFile)


if (__name__ == "__main__"):
    main()
