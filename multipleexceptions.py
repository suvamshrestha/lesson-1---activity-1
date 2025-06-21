try:
    num1,num2 = eval(input("enter two numbers: "))
    result = num1 / num2
    print("result is", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except SyntaxError:
    print("Error: Invalid input syntax. Please enter two numbers separated by a comma.")
except :
    print("wrong input")
else:
    print("No exceptions occurred, result is", result)
finally:
    print("Execution completed.")                    