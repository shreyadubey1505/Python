print("Welcome to the haunted house adventure!")
print("\nYou have to find a way to escape the haunted house.")
print("\nYou have two choices.")
print("\nEither choose to enter Room 1 or Room 2.")
stage1 = input("Which room do you want to enter? (1/2): ")
if stage1 == "1":
   print("\nWelcome")
   print("\nYou have entered Room 1.")
   print("\nYou are in a dark room.")
   print("\nYou have two choices.")
   print("\nEither choose to light a candle or walk in dark.")
   stage2 = input("What do you want to do? (Candle/Dark): ")
   if stage2 == "Candle":
      print("\n congratulations")
      print("\nBy litting a candle you got a secret key to escape.")
      print("\nYou have won the game.")
   else:
      print("\nYou are eaten by a ghost.")
      print("\nGAME OVER")
      print("\nYou have lost the game.")
      print("\nBetter luck next time.")
elif stage1 == "2":
   print("\nWelcome")
   print("\nYou have entered Room 2.")
   print("\nThere's an old chest in the corner.")
   print("\nYou have two choices.")
   print("\nEither choose to open the chest or ignore it.")
   stage2 = input("What do you want to do? (Open/Ignore): ")
   if stage2 == "Open":
      print("congratulations")
      print("\nYou found a secret key to escape.")
      print("\nYou have won the game.")
   else:
      print("\nYou are eaten by a ghost.")
      print("\nGAME OVER")
      print("\nYou have lost the game.")
else:
   print("Invalid choice.")
   print("\nYou have entered the wrong room.")
   print("\nGAME OVER")
   print("\nYou have lost the game.")
   print("\nBetter luck next time.")

# OUTPUT
# Welcome to the haunted house adventure!
#You have to find a way to escape the haunted house.
#You have two choices.
#Either choose to enter Room 1 or Room 2.
#Which room do you want to enter? (1/2): 1
#Welcome
#You have entered Room 1.
#You are in a dark room.
#You have two choices.
#Either choose to light a candle or walk in dark.
#What do you want to do? (Candle/Dark): Candle
# congratulations
#By litting a candle you got a secret key to escape.
#You have won the game.
# OR
# Welcome to the haunted house adventure!
#You have to find a way to escape the haunted house.
#You have two choices.
#Either choose to enter Room 1 or Room 2.
#Which room do you want to enter? (1/2): 2
#Welcome
#You have entered Room 2.
#There's an old chest in the corner.
#You have two choices.
#Either choose to open the chest or ignore it.
#What do you want to do? (Open/Ignore): Open
#congratulations
#You found a secret key to escape.
#You have won the game.
# OR
# Welcome to the haunted house adventure!
#You have to find a way to escape the haunted house.
#You have two choices.
#Either choose to enter Room 1 or Room 2.
#Which room do you want to enter? (1/2): 3
#Invalid choice.
#You have entered the wrong room.
#GAME OVER
#You have lost the game.
#Better luck next time.
