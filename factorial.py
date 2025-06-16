def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)
print("the factorial of 1 is", factorial(1))
print("the factorial of 2 is", factorial(2))
print("the factorial of 3 is", factorial(3))
print("the factorial of 4 is", factorial(4))
print("the factorial of 5 is", factorial(5))

