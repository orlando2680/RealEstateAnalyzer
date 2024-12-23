# Compound Interest Calculator
# Program for Calculate monthly compounded interest and determine months to reach a goal.
# By Orlando Perez.
# 11/22/2024

# The Initial deposit. part 1
while True:
    try:
        fltDeposit = float(input("Enter the initial deposit amount: "))
        if fltDeposit <= 0:
            raise ValueError("The deposit must be greater than zero.")
        break
    except ValueError as e:
        print(f"Error: {e}")


# The annual interest rate. part 2
while True:
    try:
        fltAnnualInterest = float(input("Enter the annual interest rate (in %): "))
        if fltAnnualInterest <= 0:
            raise ValueError("The annual interest rate must be greater than zero.")
        break
    except ValueError as e:
        print(f"Error: {e}")


# The number of months. part 3
while True:
    try:
        intMonths = int(input("Enter the number of months: "))
        if intMonths <= 0:
            raise ValueError("The number of months must be greater than zero.")
        break
    except ValueError as e:
        print(f"Error: {e}")


# The savings goal. part 4
while True:
    try:
        fltGoal = float(input("Enter your savings goal amount (0 if no goal): "))
        if fltGoal < 0:
            raise ValueError("The goal amount cannot be negative.")
        break
    except ValueError as e:
        print(f"Error: {e}")


# Converting annual interest rate to monthly interest rate. part 5
fltMonthlyInterestRate = (fltAnnualInterest / 100) / 12


# this is the Calculate balance for each month. part 6
print("\nMonthly Balance Breakdown:")
fltCurrentBalance = fltDeposit
for intMonth in range(1, intMonths + 1):
    fltMonthlyInterestAmount = fltCurrentBalance * fltMonthlyInterestRate
    fltCurrentBalance += fltMonthlyInterestAmount
    print(f"Month {intMonth}: Current balance: ${fltCurrentBalance:.2f}")


# Months needed to reach the savings goal. part 7
if fltGoal > 0:
    fltCurrentBalance = fltDeposit
    intMonthsToGoal = 0
    while fltCurrentBalance < fltGoal:
        fltMonthlyInterestAmount = fltCurrentBalance * fltMonthlyInterestRate
        fltCurrentBalance += fltMonthlyInterestAmount
        intMonthsToGoal += 1
    print(f"\nIt will take {intMonthsToGoal} months to reach your savings goal of ${fltGoal:.2f}.")
else:
    print("\nNo savings goal provided. Goal calculation skipped.")
