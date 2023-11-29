#Path to file
from classes.guitar import Guitar
from classes.user import User

ruben = Guitar("Gibson", "Strato", 8)
# billy = Guitar("Martin", "Strat", 8)
# tyler = Guitar("Les Paul", "X", 8)
# kyle = Guitar("Fender", "Stratocaster", 8)

cihan = User("Cihan", "Akbaba", 21)

ruben.play().stop_play()
ruben.change_strings(25)
# Guitar.num_of_guitars
print(Guitar.num_of_guitars)

cihan.play_guitar()

# print(ruben.num_of_guitars())


# billy.play().stop_play()
# billy.change_strings(19)

# tyler.play().stop_play()
# tyler.change_strings(9)

# kyle.play().stop_play()
# kyle.change_strings(1)