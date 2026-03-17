# # a = int(input("enter a number"))
# # if a % 1 == 0:
# #   c=
# #   print("total =", a)

# import random
# for i in range(10):
#   print(random.randint(1, 100))
# import random

# emojis = ["😀", "😂", "😍", "😎", "😢", "🤩", "😡", "🐱", "🐶", "🍕"] 

# print("Random Emojis:")
# for i in range(5):
#     print(random.choice(emojis))

# import random

# numbers =[]
# for i in range(10):
#   numbers.append(random.randint(1, 100))
# print(numbers)

# total=0
# for sum in numbers:
#     total+=sum

# print(total)

# HANGMAN GAME
import random
Words=["Absurd", "Arogant", "Irresponsible", "Impolite", "Uncivilized", "Uncultured", "Uneducated", "Unintelligent", "Uninformed", "Unimaginative",]
Choosen_words = random.choice(Words)
Guess = input("Guess a letter: ").lower()
if Guess  in Choosen_words:
    print("Right")
for i in range(len(Choosen_words))
    if Choosen_words[i] == Guess:
       [i] = Guess

