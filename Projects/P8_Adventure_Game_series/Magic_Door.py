print(" Welcome to The Magic Door Game! ")
print("\nYou find three doors in front of you: Red, Green, and Blue.")
door = input("Which door do you choose?(red/green/blue):")

if door == "red":
    print("\n You have entered the Fire World!")
    print(
        "\nYou have two choices, either walk through the flames or find water."
    )
    choice = input(
        "Do you want to walk through the flames or find water? (walk/find): ")

    if choice == "find":
        print("\nCongratulations!")
        print("\n You found a magic waterfall and survived the Fire World! ")
    else:
        print("\nThe flames were too strong. You got burned. Game Over!")

elif door == "green":
    print("\n You have entered the Jungle World!")
    print("\nYou have two choices, either climb a tree or explore the cave.")
    choice = input(
        "Do you want to climb a tree or explore the cave? (climb/explore): ")

    if choice == "climb":
        print("\nCongratulations!")
        print(
            "\n You climbed safely and found a hidden treasure on top of the tree!"
        )
    else:
        print("\n Oh no! The cave was full of wild animals. Game Over!")

elif door == "blue":
    print("\nYou have entered the Ice World!")
    print("\nYou have two choices, either build a fire or search for shelter.")
    choice = input(
        "Do you want to build a fire or search for shelter? (fire/shelter):")

    if choice == "shelter":
        print(
            "\n You found an ice cave to rest and survived the freezing cold!")
    else:
        print(
            "\nYou tried to build a fire but froze before it lit. Game Over!")

else:
    print(
        "\n Invalid choice! The doors vanish into thin freezing air. Game Over!"
    )

# OUTPUT
#  Welcome to The Magic Door Game!
# You find three doors in front of you: Red, Green, and Blue.
# Which door do you choose?(red/green/blue):red
#  You have entered the Fire World!
# You have two choices, either walk through the flames or find water.
# Do you want to walk through the flames or find water? (walk/find):find
# Congratulations!
#  You found a magic waterfall and survived the Fire World!
# OR
#  Welcome to The Magic Door Game!
# You find three doors in front of you: Red, Green, and Blue.
# Which door do you choose?(red/green/blue):green
#  You have entered the Jungle World!
# You have two choices, either climb a tree or explore the cave.
# Do you want to climb a tree or explore the cave? (climb/explore):climb
# Congratulations!
#  You climbed safely and found a hidden treasure on top of the tree!
# OR
#  Welcome to The Magic Door Game!
# You find three doors in front of you: Red, Green, and Blue.
# Which door do you choose?(red/green/blue):blue
# You have entered the Ice World!
# You have two choices, either build a fire or search for shelter.
# Do you want to build a fire or search for shelter? (fire/shelter):shelter
#  You found an ice cave to rest and survived the freezing cold!
# OR
#  Welcome to The Magic Door Game!
# You find three doors in front of you: Red, Green, and Blue.
# Which door do you choose?(red/green/blue):red
#  You have entered the Fire World!
# You have two choices, either walk through the flames or find water.
# Do you want to walk through the flames or find water? (walk/find):walk
# The flames were too strong. You got burned. Game Over!
