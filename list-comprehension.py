import numpy as np

# List Comprehension - iterate over an iterable and (optionally) do something
# with the items, then put them into a list

# When and when not to use List Comprehension
# 1. List Comp loads the entire output list into memory. This is acceptable for small/medium sized list because it
# makes the operation faster.
# 2. When working with large lists (million/billion elements), avoid list comprehension. It can cause a large memory
# requirement and may crash the computer.

# basic list comp syntax
# [expression for element in iterable if condition]

# example 1 - basic
a = [2, 4, 5, 6, 7, 15]
b = [x for x in a if x > 5]
print(b)

# example 2 - perform an action before adding to new list
b = [x*2 for x in a if x > 5]
print(b)

# example 3 - list of strings
names = ['Adam S', 'Candace', 'Brad', 'Jim', 'Kevaughn', 'Abbas', 'Adam R']
extracted_names = [name for name in names if name.lower().startswith('a')]
print(extracted_names)

extracted_names = [name for name in names if name.lower().__contains__('ad')]
print(extracted_names)

# example 4 - an iterable does not have to be a list, it can be any python iterable.

# lets take a 2d numpy array for ex.
matrix = np.random.randint(100, size=(4, 6))
print(matrix)

max_row_element = [max(i) for i in matrix]
print(max_row_element)

# lets take a list of lists
list_of_lists = [[2, 3, 4], [5, 1, 2], [8, 9, 3]]
max_in_list = [max(x) for x in list_of_lists]
print(max_in_list)

# example 5 - multiple conditions
extracted_names = [name for name in names if name.lower().startswith('a') and name.lower().__contains__('s')
                   and name.__contains__(' ')]
print(extracted_names)

extracted_names = [name for name in names if name.lower().startswith('a') | name.lower().endswith('e')]
print(extracted_names)

# example 6 - nested list comprehensions. they represent nested for loops.

# lets take each element out of 'list_of_lists' and put them into one list.
new_list = [y for x in list_of_lists for y in x]
print(new_list)

# this is how a nested for loop would look performing the same action
new_list = []
for y in list_of_lists:
    for x in y:
        new_list.append(x)
print(new_list)

# example 7 - nested list comps with conditions
new_list = [y for x in list_of_lists for y in x if y>3]
print(new_list)
