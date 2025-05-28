char = input("Enter a character: ")

if len(char) == 1:
    if ord(char) < 128:
        print(f"The ASCII value of '{char}' is {ord(char)}")
    else:
        print("That character is not in the ASCII range.")
