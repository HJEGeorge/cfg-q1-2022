import random
#
# random_integer = random.randint(1, 100)
#
# print(random_integer)


sides = int(input('How many sides does the die have? '))
random_integer = random.randint(1, sides)

print('You rolled a {}'.format(random_integer))
