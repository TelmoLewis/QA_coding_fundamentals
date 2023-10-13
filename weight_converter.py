print("""=================
WEIGHT CONVERTER
=================""")

weight = float(input("What is you weight? "))
unit = input("kg or lbs: ").lower()

if unit == "kg":
    print("that is you weight in lbs", (weight * 2.2))

elif unit == "lbs":
    print("that is you weight in kg", weight / 2.2)

else:
    print("not right conversion unit")