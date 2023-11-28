# Loops in Python

# Two major types of loops: for loops and while loops.

# for i in range(5, 11, 1):
#     print(i)

# print(range(1, 5))

muppets = [
    {"name": "Kermit the Frog", "location": "The swamp. I'm a frog."}, #0
    {"name": "Miss Piggy", "location": "The green room. Where's my champagne?"}, #1
    {"name": "Fozzie Bear", "location": "The Comedy Store - tonight at 8!"}, #2
    {"name": "Gonzo the Great", "location": "Waiting to be shot out of a cannon."}, #3
]

# for muppet in range(len(muppets)):
#     print(muppets[muppet]["name"])

# for muppet in muppets:
#     print(muppet["name"])

## Homework: How would we target a specific name?

'''
while condition:
    code block to be executed
'''

count = 0
while count < 500:
    print(count)
    count += 1