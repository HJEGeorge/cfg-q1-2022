price = float(input('How much is a burger? '))
person_buying = str(input("Who's paying? "))

within_budget = price <= 10.00
not_me_paying = (person_buying.lower() != "me")

print(f'Burger is within budget: {within_budget or not_me_paying}')
