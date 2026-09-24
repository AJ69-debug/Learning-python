for number in range(1,51):
  if number%3 == 0:
    print("Fizz")
  elif number%5 == 0:
    print("Buzz")
  if number%3 == 0 and number%5 == 0:
    print("FizzBuzz")
  else:
    print(number)