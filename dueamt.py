total_bill = int(input("Enter total bill amount: Rs. "))
amount_paid = int(input("Enter amount paid by customer: Rs. "))
due_amount = total_bill - amount_paid
if due_amount > 0:
    print("Customer still owes: Rs.", due_amount)
elif due_amount < 0:
    print("Extra paid: Rs.", abs(due_amount))
else:
    print("No due amount. Bill fully paid.")
