def getIncomeTax(salary):
    personal_allowance = 11850  # Personal allowance

    if salary <= personal_allowance:
        return 0  # No tax if income is within the personal allowance

    if salary <= 34500:
        return (salary - personal_allowance) * 0.20  # Taxed at 20%

    if salary <= 150000:
        return (34500 - personal_allowance) * 0.20 + (salary - 34500) * 0.40  # Taxed at 40%

    return (34500 - personal_allowance) * 0.20 + (150000 - 34500) * 0.40 + (salary - 150000) * 0.45  # Taxed at 45%

# Example usage:
salary = 150000  # Change this to test different income levels
tax = getIncomeTax(salary)
print("Income Tax: £{:.2f}".format(tax))

