maths = int(input("Enter maths marks: "))
science = int(input("Enter science marks: "))
english = int(input("Enter english marks: "))
social = int(input("Enter social marks: "))
sum = maths + science + english + social
print("Total marks: ", sum)
percentage = (sum / 400) * 100
print("Percentage: ", percentage)