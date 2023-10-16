min = 1
max = 100
secret_number = 50


for x in range(3):
    user_input = int(input(f"Enter a value between {min} and {max}: "))
    if user_input == secret_number:
        print(user_input)
        break
    elif user_input >= 1 or user_input <= 100:
        print(user_input)
        
else:
    print("None")

