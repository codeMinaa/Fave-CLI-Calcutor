print("1. add")
print("2. subtract")
print("3. divide")
print("4. multiply")
print("5. exit")
choice = input("choose an option")  
if choice not in ("1","2","3","4","5"):
    print("invalid number: please enter a valid number")

elif choice == "5":
    print("exit")
else:
        
    num1 = float(input("enter first number"))
    num2 = float(input("enter second number"))
    if choice == "1":
        result = num1 + num2
        if result .is_integer():
            print(int(result))
        else:
           print(result)

    elif choice == "2":   
        result = num1 - num2
        if result .is_integer():
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
              
        if result .is_integer():
            print(int(result))
        else:
            print(result)
       
