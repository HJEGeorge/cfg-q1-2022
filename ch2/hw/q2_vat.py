def calculate_vat(amount: float) -> float:
    return amount * 1.2


total = calculate_vat(100)
print(total)


# What's wrong? -> The function `calculate_vat` makes the calculation, but doesn't return the value.

# def calculate_vat(amount):
#     return amount * 1.2
#
# total = calculate_vat(100)
# print(total)
