try:
    age = int(input("Enter your age: "))
    if age <= 0 or age > 150:
        print("Invalid age entered!")
    else:
        print("Age is valid.")
        if age % 2 == 0:
            print("Your age is even.")
        else:
            print("Your age is odd.")
finally:
    print("age not valid")            
