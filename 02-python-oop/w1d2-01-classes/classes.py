class Guitar:
    #also known as dunder __init__.
    def __init__(self, brand, model, num_of_strings = 6):
        self.brand = brand
        self.model = model
        self.num_of_strings = num_of_strings
        self.is_playing = False
    
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

ruben = Guitar("Gibson", "Strato", 8)
billy = Guitar("Martin", "Strat", 8)
tyler = Guitar("Les Paul", "X", 8)
kyle = Guitar("Fender", "Stratocaster", 8)

ruben.play().stop_play()
ruben.change_strings(25)

billy.play().stop_play()
billy.change_strings(19)

tyler.play().stop_play()
tyler.change_strings(9)

kyle.play().stop_play()
kyle.change_strings(1)