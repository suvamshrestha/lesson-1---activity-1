a = 1
b = 2
c = 3
print(a != b)  # True
print(a != c)  # True
a = "bird"
b = "bat"
if a != b:
    print("a and b are not equal")  # a and b are not equal
a = 1 
b = 1
if (a == 1) != (b == 1):
    print("a and b are not equal")  # This will not be printed
a = int(input("Enter a number: "))
if a % 2 != 0:
    print("a is not even")  # This will be printed if a is odd