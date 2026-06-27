def calculate_due_amount(total_bill, amount_paid):
    remaining_due = total_bill - amount_paid

    print(f"Total Bill: ${total_bill:.2f}")
    print(f"Amount Paid: ${amount_paid:.2f}")
    if remaining_due > 0:
        print(f"Remaining Due: ${remaining_due:.2f}")
    elif remaining_due < 0:
        credit = abs(remaining_due)
        print(f"Status: Fully Paid.Account Credit: ${credit:.2f}")
    else:
        print("Status: Fully Paid. No remaining due or credit.") 
    return remaining_due


calculate_due_amount(total_bill=100.00, amount_paid=75.00)