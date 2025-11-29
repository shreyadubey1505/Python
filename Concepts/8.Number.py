#How to Reverse a number

# input->123->321

# take input from user
num = int(input("Enter a number: "))
store = 0           # store the reverse number

# how many digitsarethere are in num variable
l=len(str(num))     # length of the number so that loop runs 3 times
# print(l)
# loop
for i in range(1,l+1): 
  # remainder
  rem=num%10
  # store 
  store=store*10+rem
  # update num
  num=num//10

print(store) 

# OUTPUT
# Enter a number: 123
# 321


 # Armstrong Number=> 153 = 1^3 + 5^3 + 3^3 = 153

# take input from user
num=int(input("Enter a number: "))
# copy the number
copy = num
# store the sum of cubes of digits
sum=0
# how many digits are in num variable
l=len(str(num))
# loop
for i in range( l):
  # remainder
  rem=num%10
  sum=sum+rem**3
  num=num//10
print(sum)
if sum==copy:
  print("Armstrong Number")
else:
  print("Not Armstrong Number")

# OUTPUT
# Enter a number: 153
# 153
# Armstrong Number

# Perfect Number
# TAKE input from user
num = int(input("Enter a number: "))
 # store the sum of divisors   starts from 0
divisors = 0      

for i in range(1, num):      # loop runs from 1 to num
   divisors += i *(num % i == 0)        # if num is divisible by i then add i to divisors
print(divisors) 

# OUTPUT
# Enter a number: 6
# 6