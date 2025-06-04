from walking import Llama, Donkey, Goat, Pig, Horse
from slithering import BoaConstrictor, Copperhead, KingSnake, RatSnake, WaterMoccasin
from swimming import Frog, Goldfish, Koi, Mallard, Turtle
from datetime import date


def print_animal(animal):
    print(f"Name: {animal.name}")
    print(f"Species: {animal.species}")
    print(f"Date Added: {animal.date_added}")
    print()


miss_fuzz = Llama("Miss Fuzz", "domestic llama")
donkey_doo = Donkey("Donkey Doo Doo", "some kinda donkey")
billy = Goat("Billy The Goat", "Goat")
porky_porkstein = Pig("Porky Porkstein", "Bacon Pig")
domination = Horse("The Dominator", "Pure Bred Race Horse")

bitey = Copperhead("Bitey the Copperhead", "North American Copperhead Snake")
eatsrats = RatSnake("Rat Elminator", "Rat Snake")
albertking = KingSnake("Albert the King of All Snakes", "King Snake")
olbob = WaterMoccasin("Ole' Bob The Sailor", "Water Moccasin")
tightgrip = BoaConstrictor("Tight Grip McBoa", "Boa Constrictor")

chuck = Mallard("Chuck the Mallard", "Mallard Duck")
bob = Goldfish("Bob the GoldFish", "Common GoldFish")
george = Turtle("Lonesome George", "Galapagos Turtle")
kermit = Frog("Kermit the Frog", "Frog made from foam and magic")
koie = Koi("Koie the Koi Fish", "Eastern Chinese Koi Fish")


print_animal(miss_fuzz)
print_animal(donkey_doo)
print_animal(billy)
print_animal(porky_porkstein)
print_animal(domination)
print_animal(bitey)
print_animal(eatsrats)
print_animal(albertking)
print_animal(olbob)
print_animal(tightgrip)
print_animal(chuck)
print_animal(bob)
print_animal(george)
print_animal(kermit)
print_animal(koie)

# End-of-file (EOF)
