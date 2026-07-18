while True:
    password = input("Enter your password: ")

    if len(password) < 8:
        print("Weak password: Password must be at least 8 characters long.")
    elif not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        print("Weak password: Password must contain both uppercase and lowercase letters.")
    elif not any(char.isalpha() for char in password):
        print("Weak password: Password must contain at least one letter.")
    elif not any(not char.isalnum() for char in password):
        print("Weak password: Password must contain at least one special character.")
    else:
        print("Strong password!")
        break
