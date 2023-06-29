# This is the same as with exercise 16.1 only that the 6 target.write() lines have been reduced to one. The result is still the same
# The expression target.truncate has also been removed as openning the file with the "w" parameter truncates the file
from sys import argv

script, filename = argv
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
input("?")
print("Opening the file...")
target = open(filename, "w")
print("Truncating the file. Goodbye!")
print("Now I'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
print("I'm going to write these to the file.")
target.write(f"{line1}\n{line2}\n{line3}\n")
print("And finally, we close it.")
target.close()
