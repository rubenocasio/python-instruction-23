
"""
We can use a multi line string literal
as a multi line comment
"""
'''
We can use a multi line string literal
as a multi line comment
'''

#variables
#used to store data in a way we can reference by it's name
snake_case = "all lowercase separated by underscores"
# print(snake_case)

"""
PRIMITIVE (SIMPLE) DATATYPES
- Strings (str)
- Integers (int)
- Floating Point Numbers (float)
- Booleans (bool)
- None (NoneType)
"""

"""
=== === Strings === ===
Strings represent sequences of characters enclosed
in quotes.

"""
# String creation:
# print("this is a literal string".capitalize())
# print("this is a literal string".upper())
# print("this is a literal string".title())

regular_string = "Hello World"
multiline_string =""" This is a
multi-line string
in our stack!
"""
# print(multiline_string)

escaped_string = "Lauren said, \"Python is awesome!\" "
# print(escaped_string)

# Literal assignment:
my_string = "This is it"
# print(my_string)
# print(my_string.center(100, "*"))

# Constructor function:
my_other_string = str("Another string?")
# print(my_other_string)

my_number = 25
# print(type(str(my_number)))
stringified = str(my_number)
# print(type(my_number))

# Print function
# print(type(my_number))

# Type function
# print(type(my_number))

# Concatenation
hello = "Hello "
world = "World$"

# print(hello + world)
hello_world = hello + world
# print(hello_world)

# print(hello_world + 5 ) #TypeError

# print(hello_world + str(5)) #Fix


# String Methods
# print(hello_world.rsplit(" ", 3))

# length
# print(len(hello_world))

# strip
whitespace_noise = "             this is noise!              "
stripped = whitespace_noise.strip()
# print(stripped)

# string indices, index ranges
# print(hello_world[10])

# Explore more string methods!

"""
=== === BOOLEANS === ===
"""
# Literal assignment
is_awake = True
has_been_awake = False

"""
=== === INTEGERS AND FLOATS === ===
"""
# Integer literal assignment
num_of_students = 11

# Float literal assignment
pi = 3.14159

# Arithmetic operations
# +, -, *, /, **, //
# print(2**3)
# print(9 // 2)

# +=, -=, *=, /= assignment operators
x = 2
x = x + 8
x += 2

# Built-in functions for numbers
# abs, round

# Math module
import math

# sqrt, ceil, floor
print(math.sqrt(9))
print(math.ceil(pi))
print(math.floor(pi))


"""
=== === NONE === ===
"""
# Why use None?
# Represents the absence of a value or a null value
def func_with_no_return():
    print("This function has no return value")

result = func_with_no_return()
if result is None:
    print("No value returned")