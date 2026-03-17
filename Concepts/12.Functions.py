Functions : to cteate a function we use def keyword
def function_name():
  print("Hello")
  print("Bye")
function_name()   # calling the function  


def mini_cats():
  print("Hello")
  print("Bye")
mini_cats()
mini_cats()



# Adding parameters to a function
def greet(name , age):
  print(f"Hello {name} , you are {age} years old")
greet("John","20")
# OUTPUT
# Hello John , you are 20 years old

def sum(a,b):
  print(a+b)
sum(13,14)
# OUTPUT
# 27


a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
add = sum(a,b)
print(add)
# OUTPUT
# Enter a number: 13
# Enter a number: 14
# 27


# types of function : with return type , without return type
# with return type
def add(a,b):
  return a+b
result = add(2,3)
print(result)
# print(a+b) # print(a+b)  # this will not work because return type is not defined

# wihout return type
def add(a,b):
  print(a+b)
add(2,3)

# one simple example
def test():
  print("Hello")  
x = test()
print(x)       #x stores the return value of the function test() which is None.
# OUTPUT
# Hello
# None
# None is a special value in Python that represents the absence of a value or a null value.
# None is not the same as 0, False, or an empty string. None is a data type of its own (NoneType) that indicates the absence of a value.
# None is often used to indicate that a variable has not been assigned a value yet, or that a function does not return a value.

