"""
Python Functions
"""
# def greet(name):
#     print("Hello, " + name)
# greet("Tyler")

"""
The return keyword
"""
def kyle(placeholder):
    return f"Hello, {placeholder}"
print(kyle("Steven"))


"""
Scope in functions

"""
x = 3
y = 4
hello = "Hello"

def multiply(a, b):
    result = a * b
    print(hello)
    # return result
product = multiply(x, y)
print(product)