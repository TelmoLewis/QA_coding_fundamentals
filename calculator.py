first_number = int(input("enter firts number: "))
second_number = int(input("enter second number: "))

print("add +\nsubtract -\nmultiply *\ndivide /\nsquare **")

operator = input("choose a operator: ")
if operator == "+":
    print(first_number + second_number)
elif operator == "-":
    print(first_number - second_number)
elif operator == "*":
    print(first_number * second_number)
elif operator == "/":
    print(first_number / second_number)
elif operator == "**":
    print(first_number ** second_number)