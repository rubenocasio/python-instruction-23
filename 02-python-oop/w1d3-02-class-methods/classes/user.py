from classes.guitar import Guitar

class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.guitar = Guitar("Les", "Paul")

    
    def display_info(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"My age is {self.age}")
    
    def play_guitar(self):
        print("I'm playing from the Guitar class")
        self.guitar.play()
    
    def stop_guitar(self):
        self.guitar.stop_play()