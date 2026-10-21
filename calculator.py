

while True:
    print("1.add")
    print("2.sub")
    print("3.div")
    print("4.mul")
    print("5.exit")

    choice = input("enter an option: ")

    if choice not in ("1", "2", "3", "4", "5"):
        print("invalid choice: please select a valid choice")

    elif choice == "5":
        print("exit")
        break

    else:
        num1 = float(input("enter first number: "))
        num2 = float(input("enter second number: "))

        if choice == "1":
            result = num1 + num2
            if result.is_integer():
                print(int(result))
            else:
                print(result)

        elif choice == "2":
            result = num1 - num2
            if result.is_integer():
                print(int(result))
            else:
                print(result)

        elif choice == "3":
            if num2 == 0:
                print("cannot divide by zero")
            else:
                result = num1 / num2
                print(result)

        elif choice == "4":
            result = num1 * num2
            if result.is_integer():
                print(int(result))
            else:
                print(result)
