cyclist1 = int(input("Enter the speed of cyclist 1 in km/h: "))
cyclist2 = int(input("Enter the speed of cyclist 2 in km/h: "))
cyclist3 = int(input("Enter the speed of cyclist 3 in km/h: "))
average_speed = (cyclist1 + cyclist2 + cyclist3) / 3
print("The average speed of the three cyclists is:", average_speed, "km/h")
if average_speed > cyclist1 and average_speed > cyclist2 and average_speed > cyclist3:
    print("The average speed is greater than the speed of all three cyclists.")
elif average_speed > cyclist1 and average_speed > cyclist2:
    print("The average speed is greater than the speed of cyclist 1 and cyclist 2.")
elif average_speed > cyclist1 and average_speed > cyclist3:
    print("The average speed is greater than the speed of cyclist 1 and cyclist 3.")
elif average_speed > cyclist2 and average_speed > cyclist3:
    print("The average speed is greater than the speed of cyclist 2 and cyclist 3.")
elif average_speed > cyclist1:
    print("The average speed is greater than the speed of cyclist 1.")
elif average_speed > cyclist2:
    print("The average speed is greater than the speed of cyclist 2.")
elif average_speed > cyclist3:
    print("The average speed is greater than the speed of cyclist 3.")
else:
    print("The average speed is not greater than the speed of any cyclist.")            