c = input("Enter a string: ")
d = {}
for i in c:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)