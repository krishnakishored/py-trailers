
# list_variable = [x for x in iterable]
###
shark_letters = [letter for letter in 'shark']
print(shark_letters)

###
odd_num_list = [num for num in range(1,10,2)]
print(odd_num_list)

###
fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')
fish_list = [fish for fish in fish_tuple if fish != 'octopus']
print(fish_list)

###
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)

###
nested_if_list = [x for x in range(100) if x % 3 == 0 if x % 5 == 0]
print(nested_if_list)


# This code is multiplying the items in the first list by the items in the second list over each iteration.
###
my_list = [x * y for x in [20, 40, 60] for y in [2, 4, 6]]
'''
my_list = []
for x in [20, 40, 60]:
    for y in [2, 4, 6]:
        my_list.append(x * y)
'''
print(my_list)

