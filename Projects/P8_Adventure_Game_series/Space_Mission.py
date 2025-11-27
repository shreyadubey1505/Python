print("Hello! ")
print("\nWelcome to the Space Aircraft!")
print("\nYou are on a space mission.")
print("\nYou have to find a way to return safely to the earth.")
print("\nYou have two choices.")
print("\nEither choose to go to the moon or go to the mars.")
stage1 = input("Where do you want to go? (Moon/Mars): ")
if stage1 == "Mars":
   print("\nWelcome")
   print("\nYou have entered the Mars.")
   print("\nyou have two choices.")
   print("\nEither choose to collect samples or explore the caves.")
   choice = input("What do you want to do? (Collect/Explore): ")
   if choice == "Collect":
      print("\nYou have collected some interesting samples.")
      final = input(
          "Do you want to return to the earth or keep exploring?(Earth/Explore):"
      )
      if final == "Earth":
         print("\nCongratulations")
         print(
             "\nYou have returned safely to the earth with your valuable samples."
         )
         print("\nMission Successful.")
      else:
         print("\nYou have lost your way.")
         print("\nEntered a cave full of aliens. GAME OVER")
         print("\nMission Failed!.")
elif stage1 == "Moon":
   print("\nWelcome")
   print("\nYou have landed on the Moon.")
   print("\nYou have two choices.")
   print("\nEither choose to collect samples or explore the caves.")
   choice = input("What do you want to do? (Collect/Explore): ")
   if choice == "Explore":
      print("\nYou have found a secret tunnel.")
      final = input(
          "Do you want to return to the earth or keep exploring?(Earth/Explore):"
      )
      if final == "Earth":
         print("\nCongratulations")
         print(
             "\nYou have returned safely to the earth with your valuable samples."
         )
         print("\nMission Successful.")
      else:
         print("\nYou have lost your way.")
         print("\nYou kept exploring and ran out of oxygen. GAME OVER")
         print("\nMission Failed!.")
   else:
      print(
          "\n you collected some interesting samples but your equipment malfunctioned."
      )
      print("\nGAME OVER!.")
      print("\nMission Failed!.")
else:
   print("\nInvalid choice.")
   print("\nYou have entered the wrong planet.")
   print("\nGAME OVER")
   print("\nMission Failed!.")

# OUTPUT
# Hello!
# Welcome to the Space Aircraft!
# You are on a space mission.
# You have to find a way to return safely to the earth.
# You have two choices.
# Either choose to go to the moon or go to the mars.
# Where do you want to go? (Moon/Mars): Mars
# Welcome
# You have entered the Mars.
# you have two choices.
# Either choose to collect samples or explore the caves.
# What do you want to do? (Collect/Explore): Collect
# You have collected some interesting samples.
# Do you want to return to the earth or keep exploring?(Earth/Explore): Earth
# Congratulations
# You have returned safely to the earth with your valuable samples.
# Mission Successful.
# OR
# Hello!
# Welcome to the Space Aircraft!
# You are on a space mission.
# You have to find a way to return safely to the earth.
# You have two choices.
# Either choose to go to the moon or go to the mars.
# Where do you want to go? (Moon/Mars): Moon
# Welcome
# You have landed on the Moon.
# You have two choices.
# Either choose to collect samples or explore the caves.
# What do you want to do? (Collect/Explore): Explore
# You have found a secret tunnel.
# Do you want to return to the earth or keep exploring?(Earth/Explore): Earth
# Congratulations
# You have returned safely to the earth with your valuable samples.
# Mission Successful.
# OR
# Hello!
# Welcome to the Space Aircraft!
# You are on a space mission.
# You have to find a way to return safely to the earth.
# You have two choices.
# Either choose to go to the moon or go to the mars.
# Where do you want to go? (Moon/Mars): Mars
# Welcome
# You have entered the Mars.
# you have two choices.
# Either choose to collect samples or explore the caves.
# What do you want to do? (Collect/Explore): Explore
# You have lost your way.
# Entered a cave full of aliens. GAME OVER
# Mission Failed!.
