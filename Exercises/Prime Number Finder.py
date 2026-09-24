for number in range(1,51):
    for num in range(2,51):
        if number%num != 0 or number!=num:
            print(number)
            break
        else:
            break