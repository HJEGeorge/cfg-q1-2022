dog_size = int(input('How big is the dog? '))

if dog_size > 0:
    print("Your dog is a positive number size")

elif dog_size > 75:
    # A
    print('That is a big dog')

elif dog_size < 25:
    # B
    print('That is a small dog')

else:
    # C
    print('That is an average dog')
