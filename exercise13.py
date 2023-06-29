from sys import argv

# read the WYSS section for how to run this
"""This expression below takes in four arguments which unpacks argv 
  so that it gets assigned to four variables. Four arguments are provided when running the code.
  The number of arguments given must match the number of arguments to be uunpacked
  else it would throw up an error"""
script, first, second, third = argv
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
