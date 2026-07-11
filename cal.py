#clearly a cal
num1 = float(input("Enter first number: "))
operation = input("Choose operation (+, -, *, /)")
num2 = float(input("Enter second number: "))

if operation == "+":
    result = num1 + num2

elif operation == "-":
    result = num1 - num2

elif operation == "*":
    result = num1 * num2

elif operation == "/":
    result = num1 / num2

else:
    result = "invalid operation"

print("Result:", result)