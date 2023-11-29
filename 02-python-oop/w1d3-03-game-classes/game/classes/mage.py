from classes.human import Human

class Mage(Human):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.health = 50
        self.mana = 15
    
    def attack(self, target):
        # super().attack()
        print(f"{self.name} is attacking {target.name}")
        target.defend(self.mana)