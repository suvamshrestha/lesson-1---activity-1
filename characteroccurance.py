string = str(input("Enter a string: "))
char = str(input("Enter a character to find its occurrence: "))
i = 0
count = 0
while (i < len(string)):
    if string[i] == char:
        count += 1
    i += 1
print("The character", char, "occurs", count, "times in the string.")