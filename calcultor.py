num1 = float(input("enter first number"))
num2 = float(input("enter second number"))
operation = input("/,*,+,-")
if operation == "+":
    result = num1 + num2
    if result .is_integer():
        print(int(result))
    else:
        print(result)
elif operation == "/":
    print(num1 / num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "-":
    print(num1 - num2)            