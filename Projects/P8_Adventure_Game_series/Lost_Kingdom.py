print(" Welcome to The Lost Kingdom!")
print("You are a brave warrior entering a mysterious land...\n")

first = input(
    "Do you want to Fight the dragon or Sneak through the gate? (Fight/Sneak): "
)

if first == "Sneak":
    print("\n You sneaked quietly past the dragon and entered the kingdom.")
    second = input(
        "Do you want to Take the sword or Use the shield? (Take/Use):")

    if second == "Take":
        print("\n You took the magical sword glowing with power.")
        third = input(
            "Do you want to Open the treasure door or Save villagers? (Open /Save):"
        )

        if third == "Open":
            print(
                "\nThe door opens... and you find the KING’S TREASURE!  You Win!"
            )
        else:
            print(
                "\n You saved the villagers, but the treasure vanished. Game Over!"
            )
    else:
        print(
            "\n You used the shield, but the magic key needed the sword’s power. Game Over!"
        )

else:
    print(
        "\n You tried to fight the dragon, but it was too strong! Game Over!")

# OUTPUT
#  Welcome to The Lost Kingdom!
# You are a brave warrior entering a mysterious land...
# Do you want to Fight the dragon or Sneak through the gate? (Fight/Sneak): Sneak
#  You sneaked quietly past the dragon and entered the kingdom.
# Do you want to Take the sword or Use the shield? (Take/Use): Take
#  You took the magical sword glowing with power.
# Do you want to Open the treasure door or Save villagers? (Open /Save): Open
# The door opens... and you find the KING’S TREASURE!  You Win!
# OR
#  Welcome to The Lost Kingdom!
# You are a brave warrior entering a mysterious land...
# Do you want to Fight the dragon or Sneak through the gate? (Fight/Sneak): Sneak
#  You sneaked quietly past the dragon and entered the kingdom.
# Do you want to Take the sword or Use the shield? (Take/Use): Take
#  You took the magical sword glowing with power.
# Do you want to Open the treasure door or Save villagers? (Open /Save): Save
#  You saved the villagers, but the treasure vanished. Game Over!
# OR
#  Welcome to The Lost Kingdom!
# You are a brave warrior entering a mysterious land...
# Do you want to Fight the dragon or Sneak through the gate? (Fight/Sneak): Sneak
#  You sneaked quietly past the dragon and entered the kingdom.
# Do you want to Take the sword or Use the shield? (Take/Use): Use
#  You used the shield, but the magic key needed the sword’s power. Game Over!
