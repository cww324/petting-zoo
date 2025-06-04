from walking import Llama, Donkey, Goat, Pig, Horse
from slithering import BoaConstrictor, Copperhead, KingSnake, RatSnake, WaterMoccasin
from swimming import Frog, Goldfish, Koi, Mallard, Turtle
from datetime import date


def print_animal(animal):
    print(f"Name: {animal.name}")
    print(f"Species: {animal.species}")
    print(f"Date Added: {animal.date_added}")
    if hasattr(animal, "shift"):
        print(f"Shift: {animal.shift}")
    print()


miss_fuzz = Llama("Miss Fuzz", "domestic llama", "midday", "Llama Chow")
donkey_doo = Donkey("Donkey Doo Doo", "some kinda donkey", "morning", "Donkey Food")
billy = Goat("Billy The Goat", "Goat", "midday", "Hay and stuff")
porky_porkstein = Pig("Porky Porkstein", "Bacon Pig", "midday", "hay and mud")
domination = Horse(
    "The Dominator", "Pure Bred Race Horse", "morning", "RaceHorse Alpha Food mix"
)

bitey = Copperhead(
    "Bitey the Copperhead", "North American Copperhead Snake", "snake food"
)
eatsrats = RatSnake("Rat Elminator", "Rat Snake", "rats")
albertking = KingSnake("Albert the King of All Snakes", "King Snake", "snake food")
olbob = WaterMoccasin("Ole' Bob The Sailor", "Water Moccasin", "snake food")
tightgrip = BoaConstrictor("Tight Grip McBoa", "Boa Constrictor", "snake food")

chuck = Mallard("Chuck the Mallard", "Mallard Duck", "rice")
bob = Goldfish("Bob the GoldFish", "Common GoldFish", "Goldfish Nuggets")
george = Turtle("Lonesome George", "Galapagos Turtle", "Turtle Nuggets")
kermit = Frog("Kermit the Frog", "Frog made from foam and magic", "Magical Fruit")
koie = Koi("Koie the Koi Fish", "Eastern Chinese Koi Fish", "Goldfish Nuggets")


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

print(miss_fuzz)
miss_fuzz.feed()
domination.feed()
porky_porkstein.feed()

# End-of-file (EOF)
