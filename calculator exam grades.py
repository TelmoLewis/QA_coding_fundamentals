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