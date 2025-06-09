print("Opposite Right Angle Triangles")
rows = int(input("Enter the number of rows: "))
for i in range(rows):
    for j in range(i + 1):
        print("#", end="")
    spaces = (rows - i - 1) * 2
    print(" " * spaces, end="")
    for k in range(i + 1):
        print("#", end="")
    print()
