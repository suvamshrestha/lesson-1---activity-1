num1 = int(input("Enter the base number: "))
espo = int(input("Enter the exponent number: "))
result = 1
for i in range(espo):
    result *= num1
print(f"{num1} raised to the power of {espo} is {result}")