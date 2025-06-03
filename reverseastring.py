string = input("Enter a string: ")
string1 = ('')
for i in string:
    string1 = i + string1
print("the original string is: ", string)
print("the reversed string is: ", string1)