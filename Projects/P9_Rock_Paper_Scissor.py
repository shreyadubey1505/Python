# ROCK/PAPER/SCISSORS GAME

import random

r = '''

    ___
---'   __)
      (_)
      (_)
      ()
---.(_)

'''

p = '''

    ___
---'   _)_
          __)
          ___)
         ___)
---.)

'''

s = '''

    ___
---'   _)_
          __)
       ____)
      ()
---.(_)

'''

list = [r, p, s]

print("Welcome to Rock, Paper, Scissors!")
print()

user_choice = int(
    input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors.:"))
choose = list[user_choice]
computer = random.randint(0, 2)
enemy = list[computer]

if user_choice == 0:
    if computer == 0:
        print("You Choose :")
        print(choose)
        print("Computer Choose :")
        print(enemy)
        print("It's a draw")

    elif computer == 1:
        print("You Choose :")
        print(choose)
        print("Computer Choose :")
        print(enemy)
        print("You lose")

    elif computer == 2:
        print("You Choose :")
        print(choose)
        print("Computer Choose :")
        print(enemy)
        print("You win")

elif user_choice == 1:
    if computer == 0:
        print("You Choose :")
        print(choose)
        print("Computer Choose :")
        print(enemy)
        print("You win")

    elif computer == 1:
        print("You Choose :")
        print(choose)
        print("Computer Choose :")
        print(enemy)
        print("It's a draw")

    elif computer == 2:
        print("You Choose :")
        print(choose)
        print("Computer Choose :")
        print(enemy)
        print("You lose")

elif user_choice == 2:
    if computer == 0:
        print("You Choose :")
        print(choose)
        print("Computer Choose :")
        print(enemy)
        print("You lose")

    elif computer == 1:
        print("You Choose :")
        print(choose)
        print("Computer Choose :")
        print(enemy)
        print("You win")

    elif computer == 2:
        print("You Choose :")
        print(choose)
        print("Computer Choose :")
        print(enemy)
        print("It's a draw")

# OUTPUT
# Welcome to Rock, Paper, Scissors!
# What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors.:1
# You Choose :
#     ___
# ---'   _)_
#           __)
#           ___)
#          ___)
# ---.)
# Computer Choose :
#     ___
# ---'   _)_
#           __)
#        ____)
#       ()
# ---.(_)
# You win
