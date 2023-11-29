from classes.human import Human
from classes.mage import Mage
import random

billy = Human()
david = Mage("Goliath")

while billy.health > 0 and david.health > 0:
    response = ""
    while not response == "1" and not response == "2":
        print("Would you like 1) Attack or 2) Heal" )
        response = input(">>>")
        if response == "1":
            billy.attack(david)
        elif response == "2":
            billy.heal()
        else:
            print("Please select a valid response you fool!!!")
    roll = random.randint(1,2)
    if roll == 1:
        david.attack(billy)
    else:
        david.heal()

if billy.health > 0:
    print("I'm kicking your tail!")
elif david.health <= 0:
    print("It was a bloody fight@!")
else:
    print("Let's be friends!")
    