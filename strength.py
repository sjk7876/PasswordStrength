import string
import argparse
import sys


ASCII_ART_BANNER = '''
|----------------------------------------------------------------------------|
|     ___  ____ ____ ____ _ _ _ ____ ____ ___     ___ _ _  _ ____    /\_/\   |
|     |__] |__| [__  [__  | | | |  | |__/ |  \     |  | |\/| |___   ( o.o )  |
|     |    |  | ___] ___] |_|_| |__| |  \ |__/     |  | |  | |___    > ^ <   |
|----------------------------------------------------------------------------|\n'''

ASCII_ART_NYAN = '''\n
                                                                            
      ▒▒▒▒▒▒▒▒▒▒▒▒              ████████████████████████████                
  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                            ██              
  ▒▒▒▒▒▒▒▒░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒██    ░░░░░░░░▒▒░░░░▒▒░░░░░░      ██            
  ░░▒▒░░▒▒▒▒░░░░░░▒▒▒▒▒▒░░▒▒██  ░░░░▒▒░░░░░░░░████░░░░░░░░░░  ██  ████      
  ▒▒░░░░░░░░░░░░████████░░░░██  ░░░░░░░░░░░░██▒▒▒▒██░░░░▒▒░░  ████▒▒▒▒██    
  ░░░░░░░░  ░░██▒▒▒▒▒▒████████  ░░░░░░░░░░░░██▒▒▒▒▒▒██░░░░░░  ██▒▒▒▒▒▒██    
  ░░  ░░░░  ░░████▒▒▒▒▒▒▒▒▒▒██  ░░░░░░▒▒░░░░██▒▒▒▒▒▒▒▒████████▒▒▒▒▒▒▒▒██    
  ░░    ░░░░  ░░  ████████▒▒██  ░░░░░░░░░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██    
  ░░░░  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████  ░░░░░░░░▒▒██▒▒▒▒▒▒  ██▒▒▒▒▒▒▒▒▒▒  ██▒▒▒▒██  
  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██  ░░▒▒░░░░░░██▒▒▒▒▒▒████▒▒▒▒▒▒██▒▒████▒▒▒▒██  
  ▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒██  ░░░░░░▒▒░░██▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░██  
  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒████    ░░▒▒░░░░██▒▒░░░░▒▒██▒▒▒▒██▒▒▒▒██▒▒░░░░██  
  ▓▓▓▓▓▓          ▓▓▒▒████████      ░░░░░░░░██▒▒▒▒▒▒██████████████▒▒▒▒██    
                    ██▒▒▒▒▒▒████              ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██      
                    ██▒▒▒▒██  ██████████████████████████████████████        
                    ██████      ██▒▒▒▒██      ██▒▒▒▒██  ██▒▒▒▒██            
                                  ██████        ██████    ██████            
                                                                            
'''

ASCII_ART_COOL = '''\n
    ████                  ████    
  ██▒▒▒▒██              ██▒▒▒▒██  
  ██▒▒▒▒▒▒██          ██▒▒▒▒▒▒██  
  ██▒▒▒▒▒▒▒▒██████████▒▒▒▒▒▒▒▒██  
  ██▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒██  
  ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██  
  ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██  
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
██████████████████████████████████
████  ██  ██████▒▒██  ██  ████████
██▒▒██  ██████▒▒██▒▒██  ██████░░██
██▒▒░░██████▒▒▒▒▒▒▒▒▒▒██████░░░░██
██▒▒░░░░░░▒▒▒▒▒▒██▒▒▒▒▒▒▒▒░░░░░░██
  ██▒▒▒▒▒▒▒▒▒▒██████▒▒▒▒▒▒▒▒▒▒██  
    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██    
    ██████████████████████████    
'''



# Global Password Strength Requirements
NUM_UPPER = 2
NUM_LOWER = 2
NUM_NUMBERS = 2 
NUM_SYMBOLS = 2
NUM_CHARACTERS = 14

"""
Default Password Rules
    At least 14 characters
    At least 2 uppercase
    At least 2 lowercase
    At least 2 symbols
    At least 2 numbers
    No dictionary words
    No common passwords
    Max Length 1024 characters
    
    Start with 0 points
    9   = best
    7-8 = secure
    5-6 = moderate
    3-4 = weak
    0-2 = very weak
"""


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

class Settings:
    def __init__(self):
        self.input = ""
        self.output = ""
        self.verbosity = 2


def getSettings(settings):
    # Handle parameters
    parser = argparse.ArgumentParser(description="Checks the strength of a given list of passwords",
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)    
    parser.add_argument("-i", "--input_file", help="location of the input file")
    parser.add_argument("-o", "--output_file", help="location of the output file")
    parser.add_argument("-v", "--verbosity", default="2", type=int, choices=range(1,4), help="how detailed the output should be (1-3)")
    args = vars(parser.parse_args())
    
    # Input Arguments
    settings.input = args["input_file"]
    settings.output = args["output_file"]
    settings.verbosity = args["verbosity"]
        
    # Check if input file exists
    if settings.input != None:
        try:
            inTest = open(settings.input, "r")
            inTest.close()
                
        except FileNotFoundError:
            print("File", settings.input, "not found")
            return 0


def readPasswords(settings):
    passwordList = []

    # Open files for future checks
    passF = open("data/100k_password.txt", "r", encoding="utf-8")
    commonPasswords = passF.read()
    passF.close()
    
    wordF = open("data/10k_words.txt", "r", encoding="utf-8")
    commonWords = wordF.read()
    wordF.close()

    # Grab passwords from given location
    try:
        if settings.input == None:
            print("> Enter a list of passwords, with with each password \n> on its own line and an empty line to finish.")
            inF = sys.stdin
        else:
            inF = open(settings.input, "r")
                
        line = inF.readline()
                
        while line != "":
            temp = Password("")                
            temp.password = line.rstrip()
                                    
            if temp.password == "":
                break
            # elif "nyan" in temp.password:
            #     nyan = True
            # elif "cool" in temp.password:
            #     cool = True
                                    
            temp.update(commonPasswords, commonWords)
                                                    
            passwordList.append(temp)
                    
            line = inF.readline()
                
        inF.close()
                
    except: 
        print("Error reading input file -", settings.input)
    
    return passwordList


def writePasswords(passwordList, settings):
    try:
        if settings.output == None:
            outF = sys.stdout
        else:
            outF = open(settings.output, "w")
        
        if settings.verbosity == 1:
            outF.write("Strength\tPassword\n")
            outF.write("------------------------\n")
            
            for p in passwordList:
                outF.write(p.strength + "\t" + p.password + "\n")
                
        elif settings.verbosity == 2:
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
            
        if settings.output != None:
            print("Written to file -", settings.output)
            
    except:
        print("Error writing to output file -", settings.output)


def main():
    # Fun little things
    # nyan = False
    # cool = False

    settings = Settings()

    getSettings(settings)
    
    # Print fancy jazz
    if settings.input == None or settings.output == None:
        print(ASCII_ART_BANNER)
    
    passwordList = readPasswords(settings)
    
    # for p in passwordList:
    #     print(p.password, p.score)
    
    # return 0

    writePasswords(passwordList, settings)
    
    # Print fancy jazz
    # if settings.output == None and nyan:
    #         print(ASCII_ART_NYAN)
    # if settings.output == None and cool:
    #     print(ASCII_ART_COOL)


if (__name__ == "__main__"):
    main()


"""
TODO

Split main into multiple functions
Export to csv
If no output filename provided, prompt for one
    Either create a new one or use provided one from question

"""