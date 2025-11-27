import random

toss = random.choice(["head", "tail"])
print(toss)

# OUTPUT
# head
# OR
# tail

#Second Program
number = random.randint(0, 10)
print("\n", number)

if number % 2 == 0:
    print("Head")
else:
    print("Tail")

# OUTPUT
#  5
# Tail

# Third program
number = random.randint(1, 100)

if number % 2 == 0:
    print("\nHead")
else:
    print("\nTail")

# OUTPUT
# Head

# Fourth Program
number = random.randint(1, 100)

if number % 2 == 0:
    result = "Head"
else:
    result = "Tail"

guess = input("\nGuess Head or Tail: ")

if guess == result:
    print("\nYou Win!")
else:
    print("\nYou Lose!")

print("\nCoin shows:", result)

# OUTPUT
# Guess Head or Tail: head
# You Lose!
# Coin shows: Tail

# Fifth Program
number = random.randint(1, 100)

if number % 2 == 0:
    result = "Head"
else:
    result = "Tail"

print("\nRandom Number:", number)
print(result)

# OUTPUT
# Random Number: 56
# Head
