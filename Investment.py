initial_investment = float(input("intial investment: £"))
target_value = float(input("target value: £"))
interest_rate = float(input("interest rate: %")) /100

years = 0

while initial_investment < target_value:
    initial_investment *= (1 + interest_rate)
    years += 1

print(f"it will take {years} years to grow to £{target_value}")
