print ("floyd's triangle")
rows = int(input("Enter number of rows: "))
num = 1
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(num, end=' ')
        num += 1
    print()  # Move to the next line after each row