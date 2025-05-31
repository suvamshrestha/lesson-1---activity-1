medical_cause = input("Is there a medical cause for the student's absence? (Y/N): ")
attendence_percentage = int(input("Enter the student's attendance percentage: "))
if medical_cause.upper() == 'Y':
    print("The student is eligible for the exam.")
else:
    if attendence_percentage >= 75:
        print("The student is eligible for the exam.")
    else:
        print("The student is not eligible for the exam.")   
