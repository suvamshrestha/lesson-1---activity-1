units = int(input("Enter the number of units consumed: "))
if (units <= 50):
    amount = units * 2.60
    tax = 25
elif (units <= 100):
    amount = units * 3.25
    tax = 35
elif (units <= 200):
    amount = units * 5.26
    tax = 45
elif (units > 200):
    amount = units * 8.45
    tax = 75
total = amount + tax
print("total amount to be paid: ", total)                