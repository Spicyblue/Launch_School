PERCENT = 0.01

def ask_amounts():
    bill = float(input("What is the bill? "))
    tip = float(input("What is the tip percentage? "))

    return bill, tip

def math(bill_entry, tip_entry):
    tip_amount = bill_entry * tip_entry * PERCENT
    total = bill_entry + tip_amount

    return tip_amount, total

def output(tip_amount, total_amount):
    print(f"The tip is ${tip_amount:.2f}")
    print(f"The total is ${total_amount:.2f}")

def main():
    bill_amount, tip = ask_amounts()
    tip_total, total = math(bill_amount, tip)
    output(tip_total, total)

main()
