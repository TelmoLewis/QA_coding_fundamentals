def password_checker():
    common_passwords = ["password123", "letmein","admin","qwerty"]

    user_input = input("Enter your password: ")

    if user_input in common_passwords:
        print(f"Use a safer password {user_input} is compromised!")
    
    else:
        print("Password is safe!")

password_checker()
