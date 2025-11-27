print(" Welcome to The Pirate’s Gold Adventure!")
print("\nYou’re on a pirate ship searching for hidden treasure!")

deck = input("Choose a deck — A or B: ")

if deck == "A":
    print("\nYou see a shadow approaching!")
    action = input("Do you want to Fight or Hide? ")

    if action == "Fight":
        print("\n You bravely fought the pirate and won!")
        final_choice = input("Now choose: Open chest or Sail away: ")

        if final_choice == "Open chest":
            print("\nYou found the hidden pirate gold! Congratulations!")
        else:
            print(
                "\n You sailed away safely... but the gold remains hidden forever."
            )
    else:
        print(
            "\n You hid behind barrels, but the pirates found you. Game Over!")

elif deck == "B":
    print("\nYou enter a quiet deck with treasure maps lying around.")
    action = input("Do you want to Fight or Hide? ")

    if action == "Hide":
        print("\nYou hid silently and escaped detection.")
        final_choice = input("Now choose: Open chest or Sail away: ")

        if final_choice == "Open chest":
            print(
                "\nYou quietly opened the chest and found the gold. Congratulations!"
            )
        else:
            print("\nYou sailed away safely but missed the treasure!")
    else:
        print(
            "\nYou tried to fight, but there were too many pirates! Game Over!"
        )

else:
    print("\nInvalid choice — you fell overboard! Game Over!")

print("\nThank you for playing The Pirate’s Gold Adventure!")

# OUTPUT
#  Welcome to The Pirate’s Gold Adventure!
# You  are on a pirate ship searching for hidden treasure!
# Choose a deck — A or B: A
# You see a shadow approaching!
# Do you want to Fight or Hide? Fight
#  You bravely fought the pirate and won!
# Now choose: Open chest or Sail away: Open chest
# You found the hidden pirate gold! Congratulations!
# Thank you for playing The Pirate’s Gold Adventure!
# OR
#  Welcome to The Pirate’s Gold Adventure!
# You  are on a pirate ship searching for hidden treasure!
# Choose a deck — A or B: A
# You see a shadow approaching!
# Do you want to Fight or Hide? Hide
#  You hid behind barrels, but the pirates found you. Game Over!
# Thank you for playing The Pirate’s Gold Adventure!
# OR
#  Welcome to The Pirate’s Gold Adventure!
# You  are on a pirate ship searching for hidden treasure!
# Choose a deck — A or B: B
# You enter a quiet deck with treasure maps lying around.
# Do you want to Figth or Hide? Hide
# You hid silently and escaped detection.
# Now choose: Open chest or Sail away: Open chest
# You quietly opened the chest and found the gold. Congratulations!
# Thank you for playing The Pirate’s Gold Adventure!
