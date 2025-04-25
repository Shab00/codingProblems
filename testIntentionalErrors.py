import os  # Unused import

def add_numbers(a, b):
    return a + b

# Type hinting issue: Passing a string where an integer is expected
result = add_numbers(1, "two")

def unused_function():
    pass

# Naming convention issue: Variable name doesn't follow snake_case
BadVariableName = 42

# Line too long (violates PEP8 if max-line-length is set to 79 or 88)
very_long_variable_name = "This is a very long string that exceeds the recommended line length for Python code."

print(result)
