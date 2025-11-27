print(" Welcome to The School Mystery!")
print("You are locked inside your school after hours...\n")

place = input(
    "Do you want to go to the Library or the Staff Room?(Library/Staff Room): "
)

if place == "Library":
    print("\n You quietly enter the library. It’s dark and silent...")
    action = input(
        "Do you want to Read the clue or Search the desk?(Read/Search): ")

    if action == "Search":
        print("\n You found the EXIT KEY hidden under the librarian’s desk!")
        print(" You unlocked the main door and escaped safely!")
    else:
        print(
            "\n You read the wrong clue that wasted your time. The guard caught you. Game Over!"
        )

elif place == "Staff Room":
    print("\n You enter the staff room. It smells of coffee and paper.")
    action = input(
        "Do you want to Check the drawer or Open the cabinet?(Check/Open): ")

    if action == "Check":
        print("\n You found the EXIT KEY inside the drawer!")
        print(" You unlocked the main door and escaped safely!")
    else:
        print(
            "\nThe cabinet was empty — and you triggered an alarm! Game Over!")

else:
    print("\n Invalid choice. You remained locked inside forever...")

# OUTPUT
#  Welcome to The School Mystery!
# You are locked inside your school after hours...
# Do you want to go to the Library or the Staff Room?(Library/Staff Room): Library
#  You quietly enter the library. It’s dark and silent...
# Do you want to Read the clue or Search the desk?(Read/Search): Search
#  You found the EXIT KEY hidden under the librarian’s desk!
#  You unlocked the main door and escaped safely!
# OR
#  Welcome to The School Mystery!
# You are locked inside your school after hours...
# Do you want to go to the Library or the Staff Room?(Library/Staff Room): Library
#  You quietly enter the library. It’s dark and silent...
# Do you want to Read the clue or Search the desk?(Read/Search): Read
#  You read the wrong clue that wasted your time. The guard caught you. Game Over!
