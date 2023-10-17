def odd_or_even():
    user_input = int(input("enter a number: "))

    if user_input % 2 == 0:
        return "Even"
    else:
        return "Odd"

result = odd_or_even()
