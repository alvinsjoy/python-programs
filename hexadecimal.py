mode = input("h2d or d2h? ")
if mode == "h2d":
    h = input("Enter hex: ")
    print("Decimal:", int(h, 16))
elif mode == "d2h":
    n = int(input("Enter decimal: "))
    print("Hexadecimal:", format(n, "X"))
else:
    print("Invalid mode")
