print(" Welcome to The Ocean Adventure!")
print(
    "You are exploring the mysterious deep sea in search of the Golden Pearl.\n"
)

depth = input("Do you want to Dive deep or Stay near surface? (Dive/Stay): ")

if depth == "Dive":
    print(
        "\n You dive deep into the ocean where it’s dark and full of secrets.")
    second = input(
        "Do you want to Follow the dolphin or Enter the cave?(Follow/Enter): ")

    if second == "Follow":
        print("\n The dolphin leads you safely to a glowing coral reef.")
        third = input(
            "Do you want to Collect pearls or Swim away?(Collect/Swim): ")

        if third == "Collect":
            print("\n You found the rare GOLDEN PEARL! Congratulations! ")
        else:
            print("\n You swam away and missed the treasure. Game Over!")
    else:
        print(
            "\n You entered the cave but a giant octopus blocked your way! Game Over!"
        )

elif depth == "Stay":
    print("\nYou stay near the surface, watching fish swim by.")
    second = input(
        "Do you want to Follow the dolphin or Enter the cave?(Follow/Enter): ")

    if second == "Follow":
        print("\n The dolphin was friendly but led you in circles. Game Over!")
    else:
        print(
            "\n You entered a small cave near the surface and found some shiny shells!"
        )
        third = input(
            "Do you want to Collect pearls or Swim away?(Collect/Swim): ")

        if third == "Collect":
            print("\n You found the GOLDEN PEARL hidden in a shell! You Win! ")
        else:
            print(
                "\n You swam away before discovering the treasure. Game Over!")

else:
    print("\n Invalid choice. You got lost in the ocean current. Game Over!")

# OUTPUT
#  Welcome to The Ocean Adventure!
# You are exploring the mysterious deep sea in search of the Golden Pearl.
# Do you want to Dive deep or Stay near surface? (Dive/Stay): Dive
#  You dive deep into the ocean where it’s dark and full of secrets.
# Do you want to Follow the dolphin or Enter the cave?(Follow/Enter): Follow
#  The dolphin leads you safely to a glowing coral reef.
# Do you want to Collect pearls or Swim away?(Collect/Swim): Collect
#  You found the rare GOLDEN PEARL! Congratulations!
# OR
#  Welcome to The Ocean Adventure!
# You are exploring the mysterious deep sea in search of the Golden Pearl.
# Do you want to Dive deep or Stay near surface? (Dive/Stay): Dive
#  You dive deep into the ocean where it’s dark and full of secrets.
# Do you want to Follow the dolphin or Enter the cave?(Follow/Enter): Follow
#  The dolphin leads you safely to a glowing coral reef.
# Do you want to Collect pearls or Swim away?(Collect/Swim): Swim
#  You swam away and missed the treasure. Game Over!
# OR
#  Welcome to The Ocean Adventure!
# You are exploring the mysterious deep sea in search of the Golden Pearl.
# Do you want to Dive deep or Stay near surface? (Dive/Stay): Dive
#  You dive deep into the ocean where it’s dark and full of secrets.
# Do you want to Follow the dolphin or Enter the cave?(Follow/Enter): Enter
#  You entered the cave but a giant octopus blocked your way! Game Over!
