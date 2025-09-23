import random
fruits = ["apple", "banana", "cherry", "mango"]
pick = random.choice(fruits)
print("Random fruit:", pick)

import random

num = random.randint(1, 10)  # random int between 1 and 10 (inclusive)
print("Random number:", num)



cards = [ "King", "Queen", "Jack"]
random.shuffle(cards)
print("Shuffled cards:", cards)
for card in cards:
    print(card)




