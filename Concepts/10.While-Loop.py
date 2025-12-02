# while loop executes a set of statements as long as a condition is true.
# While loop is used to run a loop indefinitely.
# Advantages of while loop is that it can be used to run a loop indefinitely.
# Disadvantages of while loop is that it can be used to run a loop indefinitely.and to stop it we need to use break statement.
# One more disadvantage is that we have to write the condition to run the loop and icremement the variable manually.


j=1
while(j<=10):
  print(j)
  j=j+1


# Break Statement: enables us to exit the loop when a certain condition is met.
# Enables a program to skip over a part of the code.
# It is used to terminate the very loop it lies within.

# For loop with break statement
for i in range(12):
   if(i==10):
      break
   print("5 X",1+i,"=",5*(i+1))
print("Loop is terminated")


# While loop with break statement
while True:
   print("Hello, World!")  # This will run indefinitely
   break   # This will stop the loop


# Decrementing while loop
count=5
while(count>0):
 print(count)
 count=count-1      # This will decrease the value of count by 1. 
   # This will run until the value of count is greater than 0.
   # This will print the value of count from 5 to 1.
   # This will stop the loop when the value of count is 0.


  # 