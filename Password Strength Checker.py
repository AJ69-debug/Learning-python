while True:
    password = input("Enter your password: ")

    if len(password) < 8:
        print("Weak password: Password must be at least 8 characters long.")
    elif password.isupper() or password.islower():
        print("Weak password: Password must contain both uppercase and lowercase letters.")
    elif password.isdigit():
        print("Weak password: Password must contain at least one letter.")
    elif password.isalnum():
        print("Weak password: Password must contain at least one special character.")
    else:
        print("Strong password!")
        break