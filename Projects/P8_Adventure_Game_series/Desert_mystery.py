print(" Welcome to The Desert Mystery!")
print("\nYou are lost in a vast desert with no one around...")

path = input("Do you want to Walk towards the sun or Wait for night? ")

if path == "Walk":
    print("\nThe heat is scorching. You need to decide quickly!")
    choice = input("Do you want to Drink water or Save water? ")

    if choice == "Save":
        print(
            "\n You conserved water and reached a caravan that rescued you! ")
    else:
        print(
            "\n You drank too much water and ran out before reaching help. Game Over!"
        )

elif path == "ruko":
    print("\n You wait for the cool night breeze.")
    choice = input("Do you want to Make fire or Sleep? ")

    if choice == "Make fire":
        print("\n The fire signals a caravan passing nearby — you are saved! ")
    else:
        print(
            "\n You slept through the night and missed the caravan. Game Over!"
        )

else:
    print("\n Invalid choice — lost forever in the desert.")

#OUTPUT
# Welcome to The Desert Mystery!
# You are lost in a vast desert with no one around...
# Do you want to Walk towards the sun or Wait for night? Walk
# The heat is scorching. You need to decide quickly!
# Do you want to Drink water or Save water? Save
# You conserved water and reached a caravan that rescued you!
# OR
# Welcome to The Desert Mystery!
# You are lost in a vast desert with no one around...
# Do you want to Walk towards the sun or Wait for night? Wait
# You wait for the cool night breeze.
# Do you want to Make fire or Sleep? Make fire
# The fire signals a caravan passing nearby — you are saved!
# OR
# Welcome to The Desert Mystery!
# You are lost in a vast desert with no one around...
# Do you want to Walk towards the sun or Wait for night? Walk
# The heat is scorching. You need to decide quickly!
# Do you want to Drink water or Save water? Drink
# You drank too much water and ran out before reaching help. Game Over!
