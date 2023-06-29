# This code takes in any arbitrary number of arguments, unpacks them into argv and passes them to print_value function
from sys import argv
from os.path import exists

script, *argv = argv


def print_values(*args):
    for arg in args:
        print(arg)


print_values(*argv)
