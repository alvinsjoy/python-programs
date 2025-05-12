mode = input("b2d or d2b? ")
if mode == "b2d":
    b = input("Enter binary: ")
    print("Decimal:", int(b, 2))
elif mode == "d2b":
    n = int(input("Enter decimal: "))
    print("Binary:", format(n, "b"))
else:
    print("Invalid mode")