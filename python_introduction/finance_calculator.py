
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expences: "))
monthly_savings = float(monthly_income) - float(monthly_expenses)
projected_savings = monthly_savings * 12 + (monthly_savings *12 * 0.05)

print("Your monthly savings are $",monthly_savings)
print("Projected savings after one year, with interest, is: $", projected_savings)