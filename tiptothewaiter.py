def total_calc(bill_amt, tip_perc):
       total = bill_amt * (1 + 0.01 * tip_perc)
       total = round(total, 2)
       print(f"the total amt is {total}")
total_calc(150,2) 