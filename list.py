num = int(input("Enter the limit: "))
a = []
p = []
n = []
for i in range(num):
    x = int(input(f"Enter the {i + 1} th number: "))
    a.append(x)
    if x > 0:
        p.append(x)
    else:
        n.append(x)
print("Positive numbers are: ", p)
print("Negative numbers are: ", n)
    