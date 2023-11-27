"""
COMPOSITE (COMPLEX) DATATYPES
- Lists (list)
- Dictionaries (dict)
"""

"""
=== === LISTS === ===
In Python, arrays are called lists. You can
create them as you would an array. Use square
brackets and comma separators.
"""

# List creation
colors = ["peachpuff", "cornflowerblue", "goldenrod", "coral", "firebrick", "aqua"]

# List indices
"""
Lists have indices just like arrays have indices in
JavaScript. They are also zero-indexed as well.
"""
# print(colors)
# print(colors[1])
# print(colors[4])

# colors[2] = "pink"
# print(colors)


# List negative indices
"""
Python supports negative indices. A -1 index will refer
to the last element in a list.
"""
# print(colors[-2])
# print(colors[-5])
# print(colors[-6])

# Common list methods
"""
There are many useful methods we can use with lists.
"""

# length
"""
Pass a list to the len() method to return the number of
elements in the list.
"""
# print(len(colors))

# for i in range(len(colors)):
    # print(i)
    # print(colors[i])
    # print(colors[i][1])

# append, remove, pop
"""
append() - adds an element to the end of a list.
remove() - removes the specified element from a list.
pop() - removes the element at the specified position
"""
colors.append("hotpink")
# print(colors)

colors.remove("goldenrod")
# print(colors)

colors.pop(1)
# print(colors)

# sort, reverse
"""
The sort() method sorts a list in ascending order in-place.
The reverse() method reverses a list.
"""
nums = [5,8,9,4,6,3]
words = ["pig", "dog", "cat", "bird", "zebra", "x"]

nums.sort()
# print(nums)
words.sort()
# print(words)

nums.reverse()
# print(nums)

words.reverse()
# print(words)

# Explore more list methods!
# https://www.w3schools.com/python/python_ref_list.asp

"""
=== === DICTIONARIES === ===
"""

# Dictionary creation
strat = {
    "brand": "Fender",
    "model": "Stratocaster",
    "year": 1977,
    "color": "blue",
    "is_new": False,
}

# Accessing values with bracket notation
"""
We can access values in a dictionary by their
key names. Use bracket notation with quotes.
"""
# print(strat["year"])
# strat["year"] = 2002
# print(strat["year"])


# Accessing values with the get() method
"""
We can access values in a dictionary with the get()
method. Pass the key name in the method call in quotes.
"""
# print(strat["ruben"])
# print(strat.get("model"))

"""
What's the difference between bracket notation and .get()?
With .get(), our application doesn't break if we specify
a key name that doesn't exist.
"""
# print(strat.get("model"))
# print(strat.get("ruben"))

# Dictionary methods
"""
There are many useful methods we can use with lists.
"""

# keys, values, items
"""
HOMEWORK
.keys() - returns an array of the dictionary's keys.
.values() - returns an array of the dictionary's values.
.items() - returns an array of tuples of the dictionary's key-value pairs.
"""

# in, not in
"""
We can use the 'in' and 'not in' keywords to check if a key
name exists in a dictionary.
"""
# if "owner" in strat:
#     print("owner in strat")
# else:
#     print("owner is not in strat")

if "model" in strat:
    print("Model is in strat")
else:
    print("Model is not in strat")

# Explore more dictionary methods!
# https://www.w3schools.com/python/python_ref_dictionary.asp
