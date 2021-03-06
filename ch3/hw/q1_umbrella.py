"""Q1
Create a program that tells you whether or not you need an umbrella when you leave the house.

The program should:
    1. Ask you if it is raining using input()
    2. If the input is 'y', it should output 'Take an umbrella'
    3. If the input is 'n', it should output 'You don't need an umbrella'
"""


raining = input("Is it raining today (y/n)? ")


if raining.lower() == "y":
    print("☔️ Take an umbrella ️")
elif raining.lower() == "n":
    print("☀️ You don't need an umbrella, enjoy the sun ️")
else:
    print("⚠️ Invalid input, please enter 'y' (yes) or 'n' (no)")
