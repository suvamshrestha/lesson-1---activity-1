print ("enter the marks obtained by the student in 5 subjects")
maths = int(input("Enter marks in Maths: "))
science = int(input("Enter marks in Science: "))
english = int(input("Enter marks in English: "))
history = int(input("Enter marks in History: "))
geography = int(input("Enter marks in Geography: "))
total_marks = maths + science + english + history + geography
average_marks = total_marks / 5
if average_marks >= 91 and average_marks <= 100:
    print("Grade: A1")
elif average_marks >= 81 and average_marks <= 91:
    print("Grade: A2")
elif average_marks >= 71 and average_marks <= 81:
    print("Grade: B1")
elif average_marks >= 61 and average_marks <= 71:
    print("Grade: B2")
elif average_marks >= 51 and average_marks <= 61:
    print("Grade: C1")
elif average_marks >= 41 and average_marks <= 51:
    print("Grade: C2")
elif average_marks >= 31 and average_marks <= 41:
    print("Grade: D")
elif average_marks >= 21 and average_marks <= 31:
    print("Grade: E1")
elif average_marks >= 11 and average_marks <= 21:
    print("Grade: E2")
else:
    print("FAIL")        

