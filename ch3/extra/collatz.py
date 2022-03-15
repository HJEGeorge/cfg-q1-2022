def collatz(number):
    if number % 2 == 0:
        number = int((number // 2))
        print(number)
    elif number % 2 != 0:
        number = int((3 * number + 1))
        print(number)
    else:
        print("That's weird")
    return number


result = int(input("Choose a number at random: "))

while result != 1:
    result = collatz(result)
