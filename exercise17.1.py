from sys import argv
from os.path import exists

script, from_file, to_file = argv
print(f"Copying from {from_file} to {to_file}")
# I have combined lines 7 and 8 of exercise 17 into one line(line 7)
in_file = open(from_file).read()
print(f"The input file is {len(in_file)} bytes long")
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()
# I have also combined the lines 13 and 14 of exercise 17 into one line(line 17)
out_file = open(to_file, "w").write()
print("Alright, all done.")
out_file.close()
in_file.close()
