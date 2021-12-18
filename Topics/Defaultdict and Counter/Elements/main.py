from collections import Counter

in_string = input()
c = Counter(in_string.lower().split())
print(sorted(c.elements()))
