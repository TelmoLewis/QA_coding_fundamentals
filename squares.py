number = 1

while number <= 100:
    square = number ** 2
    print(f"Number: {number}, Square: {square}")

    if square > 2000:
        break

    number += 1