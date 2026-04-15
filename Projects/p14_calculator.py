# Build a Calculator using functions..


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        print("Error! Division by zero.")
        return x / y


while True:
    start = input("Do you want to perform a calculation? (yes/no): ")
    if start == "no":
        break

    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    if op == "+":
        result = add(num1, num2)
    elif op == "-":
        result = subtract(num1, num2)
    elif op == "*":
        result = multiply(num1, num2)
    elif op == "/":
        result = divide(num1, num2)
    else:
        print("Invalid operator")
        continue
    print("Result is:", result)

while True:
    want_to_continue = input("Do you want to perform another calculation? (yes/no): ")
    if want_to_continue == "no":
        break

    num = float(input("Enter next number: "))
    op = input("Enter operator (+, -, *, /): ")
    if op == "+":
        result = add(result, num)
    elif op == "-":
        result = subtract(result, num)
    elif op == "*":
        result = multiply(result, num)
    elif op == "/":
        result = divide(result, num)
    else:
        print("Invalid operator")
        continue

print("Result is:", result)
print("Final result is:", result)
