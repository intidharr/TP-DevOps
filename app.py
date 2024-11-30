# A simple Python application with a function to test
def add_numbers(a, b):
    """Adds two numbers."""
    return a + b

def subtract_numbers(a, b):
    """Subtracts b from a."""
    return a - b

def multiply_numbers(a, b):
    """Multiplies two numbers."""
    return a * b

def divide_numbers(a, b):
    """Divides a by b. Raises an error if dividing by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b