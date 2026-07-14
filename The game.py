import random

while True:
    randnum = random.randint(1,20)
    attempts = 0
    print("I'm thinking of a number between 1 and 20...")
    print("Take a guess: ",end="") 
    while True:
        try:
           
            guess = int(input())
            
            
            if guess > randnum:
                print("\nToo high")
                print("try again: ",end="")
                attempts+=1
                continue
            elif guess < randnum:
                print("\nToo low")
                print("try again: ",end="")
                attempts+=1
                continue
            elif guess == randnum:
                attempts+=1
                print(f"correct, It took you {attempts} attempts to guess correctly")
                break
            else:
                raise ValueError
        except:
            print("\nInvalid input")
            print("try again: ",end="")
    
    print("\nDo you wish to play again (yes/no): ",end="")
    replay = input().lower()
    try:
        if replay == "yes":
            continue
        elif replay == "no":
            print("\nThank you for playing.")
            break
        else:
            raise valueError
    except:
        print("\nInvalid input")