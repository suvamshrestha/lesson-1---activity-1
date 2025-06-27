start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
squares = []
odd_squares = []
even_squares = []
for num in range(start, end + 1):
    square = num * num 
    squares.append(square)
    if square % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)
print("all squares:", squares)
print("even squares:", even_squares)
print("odd squares:", odd_squares)        
