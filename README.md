# PasswordStrength
This is a Python program that takes in a list of passwords as an input, and 
outputs how secure they are based on both an arbitrary guideline as well as if 
it is contained in a list of the 100k most common passwords and 10k most commond words.

# Options
Using the argparse library, there are 3 parameters you can set on start.
1. The input file can be specified with -i FILENAME or --input_file FILENAME
2. The output file can be specified with -o FILENAME or --output_file FILENAME 
3. The verbosity of the output can be specified with -v 1,2,3 or --verbosity 1,2,3
