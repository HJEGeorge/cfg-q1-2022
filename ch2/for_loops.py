# colours = ["yellow", "green", "blue", "red", "orange"]
#
# for colour in colours:
#     print(f"One colour we could use is {colour}")
#
# print("done")

# for num in range(1, 33, 2):
#     print(num)
#
#
# name = "Henry George"
#
# for var1 in name:
#     print(var1)

numbers = range(10000) # remember: 0,1,2,3,4,5,6,7,8,9

sum = 0

for num in numbers:
    sum += num # --> this syntax is equal to: sum = sum + num
    if sum > 20:
        break
    print(f'The total at this stage is: {sum}')

print('\nFinal sum is: ', sum)  