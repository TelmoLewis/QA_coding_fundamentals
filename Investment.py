investment = 100
target = 1000
interest = 0.10

years = 0

while investment < target:
    investment *= (1 + interest)
    years += 1

print(f"It will take around {years} years for investment of £100 to reach to £{target}"
