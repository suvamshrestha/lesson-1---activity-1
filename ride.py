print ("enter your ride")
print ("1. bike")
print ("2. car")
ride = input("Enter your choice (1 or 2): ")
if ride == "1":
    print ("what type of bike do you want?")
    print ("1. mountain bike")
    print ("2. road bike")
    choice = int(input("Enter your choice (1 or 2): "))
    if choice == 1:
        print ("You have chosen a mountain bike.")
    elif choice == 2:
        print ("You have chosen a road bike.")
    else:
        print ("Invalid choice. Please try again.")
elif ride == "2":
    print ("what type of car do you want?")
    print ("1. sedan")
    print ("2. SUV")
    choice = int(input("Enter your choice (1 or 2): "))
    if choice == 1:
        print ("You have chosen a sedan.")
    elif choice == 2:
        print ("You have chosen an SUV.")
    else:
        print ("Invalid choice. Please try again.")        