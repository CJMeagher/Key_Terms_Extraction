import string

in_strings = [input(), input()]
# in_strings = ["no one knows what it's like", "to be the bad man"]

print(string.capwords(in_strings[0], "*"))
print(string.capwords(in_strings[1]))
