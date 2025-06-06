num = int(input("Enter a number: "))
t = num
numLength = 0
while t > 0:
    numLength = numLength + 1
    t = int(t / 10)
if numLength >= 5:
    numLength = int(numLength / 2)
    chk = 0
    while num > 0:
        rem = num % 10
        if chk == numLength:
            midOne = rem
        elif chk == (numLength - 1):
            midTwo = rem
        num = int(num / 10)
        chk = chk + 1
    prod = midOne*midTwo
    print("The product of the middle digits is:", prod)
else:
        print("the number does not have 4 digits.")        
