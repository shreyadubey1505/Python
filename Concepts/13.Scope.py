# Scope  : Scope is the region of the program where a variable is defined.
# There are two types of scope in Python: local and global.

# Local Scope : A variable is said to be in the local scope if it is defined inside a function.
# Global Scope : A variable is said to be in the global scope if it is defined outside a function.
# Local variables are only accessible inside the function where they are defined.
# Global variables are accessible from any part of the program.
# Local variables are created when the function is called and destroyed when the function returns.
# Global variables are created when the program starts and destroyed when the program ends.
# Local variables have a higher precedence than global variables.
# If a variable is defined in both the local and global scope, the local variable will be used.

# global scope
enemies = 2
def increase_enemies():
  enemies = 5   # local scope
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
# OUTPUT
# enemies inside function: 5
# enemies outside function: 2

def cold_drink():
  # local variable
  glass = 2
  print(glass)
# output
# 2

# How to modify global variable inside a function
# global keyword is used to modify global variable inside a function
enemies = 2
def increase_enemies():
   global enemies
   enemies += 1
   print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
# OUTPUT
# enemies inside function: 3
# enemies outside function: 3