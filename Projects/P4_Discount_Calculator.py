bill = float(input("Enter your total bill:"))
if bill > 5000:
   print("You get a 20% discount")
   discount = bill * 0.2
   print("Your discount is", discount)
   print("Your final bill is", bill - discount)
elif 2000 <= bill <= 4999:
   print("You get a 10% discount")
   discount = bill * 0.1
   print("Your discount is", discount)
   print("Your final bill is", bill - discount)
else:
   print("no discount")
   print("Your final bill is", bill)

# OUTPUT
# Enter your total bill:5500
# You get a 20% discount
# Your discount is 1100.0
# Your final bill is 4400.0
# OR
# Enter your total bill:3000
# You get a 10% discount
# Your discount is 300.0
# Your final bill is 2700.0
