decimal_num = int(input("Enter a decimal number: "))
binary_num = bin(decimal_num)[2:]  # Convert to binary and remove the '0b' prefix
print(f"The binary representation of {decimal_num} is: {binary_num}")