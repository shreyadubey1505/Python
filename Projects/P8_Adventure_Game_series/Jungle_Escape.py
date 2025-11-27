print("Hello Hello!")
print("\nWelcome to the Jungle Escape Game!")
print("\nOH NO!")
print("\nYou are trapped in a jungle!")
print("\nYou have to the find the correct combination to escape safely.")
print("\nYou have 2 ways to escape.")
print("\n1. Either go left towards the river or right towards the mountain.")
Choose = input("Choose Left(L) or Right(R): ")
if Choose == "L":
   print("\nYou choosed to go to the river.Walk ahead.")
   print("\nYou got two options")
   print("\n1. Either choose to swim across the river or build a raft.")
   Choice = input("Choose Swim(S) or Build a raft(B): ")
   if Choice == "B":
      print("\n You choosed to build a raft.")
      print(
          "\n Smart choice! You successfully build a raft and crossed the river safely."
      )
      print("\n You escaped the jungle successfully.")
   else:
      print("\n You choosed to swim across the river.")
      print("\n You got eaten by a crocodile.")
      print("\n GAME OVER!")
      print("\n You failed to escape the jungle.")
elif Choose == "R":
   print("\nYou choosed to go to the mountain.Walk ahead.")
   print("\nYou got two options")
   print("\n1. Either choose to climb the mountain or rest.")
   Choice = input("Choose to Climb(C) or Rest(R): ")
   if Choice == "C":
      print("\n You choosed to climb the mountain.")
      print("\nYou climbed carefully and found a path leading to the exit.")
      print("\n You escaped the jungle successfully.")
   else:
      print("\n You choosed to rest.")
      print("\n while resting you got eaten by a Lion.")
      print("\n Game Over!.")
else:
   print(
       "\n Invalid Choice. You wanderedaimlessly in the jungle and got lost forever."
   )
   print("\n Game Over!.")

# OUTPUT
# Hello Hello!
# Welcome to the Jungle Escape Game!
# OH NO!
# You are trapped in a jungle!
# You have to the find the correct combination to escape safely.
# You have 2 ways to escape.
# 1. Either go left towards the river or right towards the mountain.
# Choose Left(L) or Right(R): L
# You choosed to go to the river.Walk ahead.
# You got two options
# 1. Either choose to swim across the river or build a raft.
# Choose Swim(S) or Build a raft(B): B
#  You choosed to build a raft.
#  Smart choice! You successfully build a raft and crossed the river safely.
#  You escaped the jungle successfully.
# OR
# Hello Hello!
# Welcome to the Jungle Escape Game!
# OH NO!
# You are trapped in a jungle!
# You have to the find the correct combination to escape safely.
# You have 2 ways to escape.
# 1. Either go left towards the river or right towards the mountain.
# Choose Left(L) or Right(R): R
# You choosed to go to the mountain.Walk ahead.
# You got two options
# 1. Either choose to climb the mountain or rest.
# Choose to Climb(C) or Rest(R): C
#  You choosed to climb the mountain.
# You climbed carefully and found a path leading to the exit.
#  You escaped the jungle successfully.
# OR
# Hello Hello!
# Welcome to the Jungle Escape Game!
# OH NO!
# You are trapped in a jungle!
# You have to the find the correct combination to escape safely.
# You have 2 ways to escape.
# 1. Either go left towards the river or right towards the mountain.
# Choose Left(L) or Right(R): L
# You choosed to go to the river.Walk ahead.
# You got two options
# 1. Either choose to swim across the river or build a raft.
# Choose Swim(S) or Build a raft(B): S
#  You choosed to swim across the river.
#  You got eaten by a crocodile.
#  GAME OVER!
#  You failed to escape the jungle.
