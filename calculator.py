def add(P,Q):
    return P + Q
def subtract(P,Q):
    return P - Q
def multiply(P,Q):
    return P * Q
def divide(P,Q):
    return P / Q 
print("which opperation would you like to perform?")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
num = input("select your choice(1,2,3,4): ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num == "1":
    print("The sum is: ", add(num1,num2))
elif num == "2":
    print("The difference is: ", subtract(num1,num2))
elif num == "3":
    print("The product is: ", multiply(num1,num2))
elif num == "4":
    print("The quotient is: ", divide(num1,num2))
else:
    print("Invalid choice, please select a valid operation.")    
