from collections import Counter

x = open("mytext", "r")
data = x.read()
print(data)

s = data
s = s.split()
l = len(s)
print(l)

counts = Counter(data)
print(counts)
