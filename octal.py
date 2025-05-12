mode = input("o2d or d2o? ")
if mode == "o2d":
    o = input("Enter octal: ")
    print("Decimal:", int(o, 8))
elif mode == "d2o":
    n = int(input("Enter decimal: "))
    print("Octal:", format(n, "o"))
else:
    print("Invalid mode")
