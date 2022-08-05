num1 = float(input("please enter the first number:"))
operator = input("please enter operator:")
num2 = float(input("please enter the next number:"))

if operator == "+":
    value = num1 + num2
elif operator == "-":
    value = num1 - num2
elif operator == "*":
    value = num1 * num2
elif operator == "/":
    value = num1 / num2
else:
    print("invalid input")

print(value)
