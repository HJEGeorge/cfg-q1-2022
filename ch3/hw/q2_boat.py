"""Q2
I'm on holiday and want to hire a boat. The boat hire costs £20 + a refundable £5 deposit. I've
written a program to check that I can afford the cost, but something doesn't seem right.
Have a look at my program and work out what I've done wrong.

my_money = input('How much money do you have? ')
boat cost = 20 + 5
if my_money < boat_cost:
print('You can afford the boat hire')
else:
print('You cannot afford the board hire')
"""
import re

# Take input as a string, but it could include £, commas, or more
my_money = input('How much money do you have? (no decimals please)')
my_money = re.sub(r"[^/d.]", "", my_money)
my_money = int(my_money)

boat_cost = 20 + 5
if my_money < boat_cost:
    print('You can afford the boat hire')
else:
    print('You cannot afford the board hire')
