# Example 1: Adding incompatible types
try:
    result = "42" + 8
    print(result)
except TypeError as e:
    print("TypeError Example 1:", e)

# Example 2: Calling a method on an object that doesn't support it
try:
    number = 123
    number.append(4)  # AttributeError: 'int' object has no attribute 'append'
except AttributeError as e:
    print("AttributeError Example 2:", e)

# Example 3: Indexing a non-subscriptable object
try:
    x = 42
    print(x[0])  # TypeError: 'int' object is not subscriptable
except TypeError as e:
    print("TypeError Example 3:", e)

# Example 4: Passing the wrong type to a function
try:
    import math
    result = math.sqrt("hello")  # TypeError: must be real number, not str
except TypeError as e:
    print("TypeError Example 4:", e)

# Example 5: Using an incompatible type with int()
try:
    x = int(5+2j)  # TypeError: int() can't convert complex to int
    print(x)
except TypeError as e:
    print("TypeError Example 5:", e)

print("\nUnlike ValueError, TypeError happens when the type itself is incompatible,")
print("not when the content is invalid for the conversion.") 