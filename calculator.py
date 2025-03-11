num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
operation = input("Enter operator(+,-,*,/):")

if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"num1 - num2 = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"num1 * num 2 = {result}")
elif operation == "/":
    result = num1 / num2
    print(f"num1 / num2 = {result}")
else:
    print("Invalid operator")
