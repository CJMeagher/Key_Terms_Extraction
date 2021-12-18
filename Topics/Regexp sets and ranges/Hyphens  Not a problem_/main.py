import re

# your code here
word = input()
if re.match("[A-Za-z]+-[A-Za-z]+", word):
    print("True")
else:
    print("False")
