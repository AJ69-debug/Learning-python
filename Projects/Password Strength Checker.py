while True:
    password = input("Enter your password: ")

    has_8char = False
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password:
        if len(password) >= 8:
            has_8char = True
        if char.isupper():
            has_upper = True
        if  char.islower():   
            has_lower = True
        if char.isdigit():
            has_digit = True
        if not char.isalnum():
            has_special = True

    
    if not has_8char:
        print("your password needs atleast 8 characters")
    if not has_upper:
        print("your password needs atleast 1 uppercase character")
    if not has_lower:
        print("your password needs atleast 1 lowercase character")
    if not has_digit:
        print("your password needs atleast 1 number")
    if not has_special:
        print("your password needs atleast 1 special character")
    else:
        print("Your password is strong")
        break
