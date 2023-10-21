math_mark = -1
english_mark = -1
ict_mark = -1

while math_mark < 0 or math_mark > 100:
    math_mark = int(input("Enter a Maths grade between 1 an 100: "))
    if math_mark < 0 or math_mark > 100:
        print("Invalid mark, please enter a mark between 1 and 100")

while english_mark < 0 or english_mark > 100:
    english_mark = int(input("Enter a english mark between 1 and 100: "))
    if english_mark < 0 or english_mark > 100:
        print("Invalid mark, please enter a mark between 1 and 100")

while ict_mark < 0 or ict_mark > 100:
    ict_mark = int(input("Enter a ICT mark between 1 and 100: "))
    if ict_mark < 0 or ict_mark >100:
        print("Invalid mark, please enter a mark between 1 and 100")

average_mark = (math_mark + english_mark + ict_mark) / 3

print(f"Average mark is: {average_mark:.2f}")

if average_mark >= 65:
    print("Pass")
elif average_mark < 65:
    print("Fail")
