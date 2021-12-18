import re

file = open("file.txt", "r")
count = 0
for line in file:
    if re.match("cool$", line):
        count += 1
print(count)
