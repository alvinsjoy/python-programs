# Define a simple custom exception
class AgeError(Exception):
    """Exception raised when age is outside allowed range."""
    pass

def verify_age(age):
    if age < 0 or age > 120:
        raise AgeError
    else:
        return f"Age {age} is valid"

# Test the exception
try:
    print(verify_age(25))    # This works fine
    print(verify_age(150))   # This will raise the exception
except AgeError as e:
    print(f"Error: {e}")
    print(f"Invalid age entered: {e}") 