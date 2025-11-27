print("The Treasure Island")
print("\nYour mission is to find the treasure.")
print("\nStage 1\n")
print(
    "\nYou are in a dark, narrow cave with only two doors.Do you want to go through door 1 or door 2?"
)
stage1 = input("Choose door 1 or door 2:")
if stage1 == "1":
  print("Congratulations you choose the correct door.")
  print("\nStage 2\n")
  print("\nNow there is a river.")
  print("\nDo you want to swim across the river or use the boat to cross it?")
  stage2 = input("Choose swim(S) or boat(B):")
  if stage2 == "B":
    print("Congratulations you crossed the river.")
    print("\nStage 3\n")
    print(
        "\nThere are three doors in front of you. Red door, Blue door and Yellow door."
    )
    stage3 = input("Choose a door (R/B/Y):")
    if stage3 == "B":
      print("Congratulations you found the treasure.")
      print("YOU WON")
    else:
      print("Sorry, you choose the wrong colour.")
      print("GAME OVER")
  else:
    print("The river had crocodile.")
    print("GAME OVER")
    print("People luckily put their hands on treasure.")

else:
  print("Sorry, you choose the wrong door.")
  print("GAME OVER")
  print("People luckily put their hands on treasure.")

# OUTPUT
# The Treasure Island
# Your mission is to find the treasure.
# Stage 1
# You are in a dark, narrow cave with only two doors.Do you want to go through door 1 or door 2?
# Choose door 1 or door 2:1
# Congratulations you choose the correct door.
# Stage 2
# Now there is a river.
# Do you want to swim across the river or use the boat to cross it?
# Choose swim(S) or boat(B):B
# Congratulations you crossed the river.
# Stage 3
# There are three doors in front of you. Red door, Blue door and Yellow door.
# Choose a door (R/B/Y):B
# Congratulations you found the treasure.
# YOU WON
# OR
# The Treasure Island
# Your mission is to find the treasure.
# Stage 1
# You are in a dark, narrow cave with only two doors.Do you want to go through door 1 or door 2?
# Choose door 1 or door 2:2
# Sorry, you choose the wrong door.
# GAME OVER
# People luckily put their hands on treasure.
