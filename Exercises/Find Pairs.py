numbers = [2, 4, 3, 5, 7, 8, 1, 9]
target = 10

for number in numbers:
    for index in range(0,len(numbers)):
        if number+numbers[index] == 10:
            print(f"({number},{numbers[index]})")