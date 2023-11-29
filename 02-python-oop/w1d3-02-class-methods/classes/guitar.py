class Guitar:

    num_of_guitars = 0 #class attribute

    #also known as dunder __init__.
    def __init__(self, brand, model, num_of_strings = 6):
        self.brand = brand
        self.model = model
        self.num_of_strings = num_of_strings
        self.is_playing = False

        # Guitar.num_of_guitars += 1

    @classmethod
    def increase_num_of_guitars(cls):
        cls.num_of_guitars += 1

    #A method to play the guitar
    def play(self):
        self.is_playing = True
        print(f"This {self.brand} {self.model} is being played!")
        return self

    #stop play
    def stop_play(self):
        self.is_playing = False
        print(f"This {self.brand} {self.model} has stopped playing!")
        return self
    
    #change strings
    def change_strings(self, new_num_of_strings ):
        self.num_of_strings = new_num_of_strings
        print(f"Changed the strings on my  {self.brand} {self.model} to {self.num_of_strings} strings.")
        return self