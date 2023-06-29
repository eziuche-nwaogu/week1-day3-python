# Reading files from a text file
# Importing argv from sys module
from sys import argv

# get argv command line arguments when running the file and assigning it to two variables
script, filename = argv
# open the filename and assign it to a variable
txt = open(filename)
# print out the filename and then open the file using read()
print(f"Here's your file {filename}:")
print(txt.read())
# Print out instructions and ask for user input using input()
print("Type another filename to be opened:")
file_again = input("> ")
# open the filename and assign it to a variable
txt_again = open(file_again)
# open the file using read()
print(txt_again.read())
