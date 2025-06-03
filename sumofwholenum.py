num1 = int(input("enter the number to find the sum of whole numbers: "))
sum = 0
for i in range(1, num1 + 1):
    sum = sum + i
print("The sum of whole numbers from 1 to", num1, "is:", sum)
