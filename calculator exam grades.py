grade = int(input("what is your grade? "))
if grade < 1 or grade > 100:
    print("marks must be between 1 and 100")
elif grade < 50:
    print("fail")
elif grade >= 50 and grade <= 60:
    print("Pass")
elif grade > 60 and grade <= 70:
    print("Merit")
elif grade > 70 and grade >= 100:
    print("Distinction")



# part 2


mark = int(input("Enter exam mark (between 1 and 100): "))
level = int(input("Enter student level (1 or 2): "))

if mark < 1 or mark > 100:
    print("Error: marks must be between 1 and 100")
elif level == 1:
    if mark < 50:
        print("Fail")
    elif mark <= 60:
        print("Pass")
    elif mark <= 70:
        print("Merit")
    else:
        print("Distinction")
elif level == 2:
    if mark < 40:
        print("Fail")
    elif mark <= 50:
        print("Pass")
    elif mark <= 65:
        print("Merit")
    else:
        print("Distinction")
else:
    print("Invalid level, please enter 1 or 2")
