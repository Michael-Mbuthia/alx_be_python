monthly_income = float(input("Enter your monthly income: "))
total_monthly_expenses = float(input("Enter your total monthly expenses: "))
# Calculate monthly savings
monthly_savings = monthly_income - total_monthly_expenses 
# Project annual savings with interest
interest_rate = 0.05
annual_savings = monthly_savings * 12
projected_savings = monthly_savings * 12 + (annual_savings * Interest_rate)

print("Your monthly savings are $", monthly_savings, ".")
print("Projected savings after one year, with interest, is: $", projected_savings, ".")
