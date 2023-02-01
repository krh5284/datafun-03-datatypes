"""
Modify this docstring.

Kellie Heckman
List practice
"""

# import some modules first - how many can you make use of?

import math
import random
import statistics as stats
import numpy as np

# define some functions


def get_area_of_lot(length, width):
    """
    Return area of a lot given the length and width of the lot.

    Could this fail?

    """

    # Use a try / except / finally block when something
    # could go wrong
    try:
        area = 0  # fix this
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None


# define more functions here (see instuctions)
# create list1, a list of 20 random numbers
list1 = []
for i in range(0,20):
    n = random.randint(1,30)
    list1.append(n)
print(f'list1: {list1}')

# create listx_practice, a random list of 10 times
listx_practice = []
for i in range(0,10):
    n = random.randint(1,10)
    listx_practice.append(n)
print(f'listx_practice: {listx_practice}')

# creat listy_practice, a random list of 10 "values", in this case number of chickens in the coop area at time "x" as the sun sets
listy_practice = []
for i in range(0,10):
    n = random.randint(1,20)
    listy_practice.append(n)
print(f'listy_practice: {listy_practice}')

# create listx and listy in a non-random way so that they're kinda linear
listx = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listy = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] 

# LIST STATISTICS
# mean, median and mode of list1, listx, and listy

print(f'List1 mean: {stats.mean(list1)}')
print(f'Listx mean: {stats.mean(listx)}')
print(f'Listy mean: {stats.mean(listy)}')

print(f'List1 median: {stats.median(list1)}')
print(f'Listx median: {stats.median(listx)}')
print(f'Listy median: {stats.median(listy)}')

print(f'List1 mode: {stats.mode(list1)}')
print(f'Listx mode: {stats.mode(listx)}')
print(f'Listy mode: {stats.mode(listy)}')

#standard deviation and variance of list1

print(f'Standard Deviation: {stats.stdev(list1)}')
print(f'Variance: {stats.variance(list1)}')

# CORRELATION AND PREDICTION
# correlation between listx and listy

print(f'Correlation: {np.cov(listx, listy)}')

# slope and intercept

intercept = np.polyfit(listx, listy,1)
print(intercept)

# predict fucntion taking slope, intercept and x to predict a y value
if __name__ == "__main__":
    def predict(slope, intercept, x): 
        y = slope * x + intercept
        print(y)


predict(2.00000000e+00, 15, -5.61733355e-15)


#  built in functions

print(f'Minimum: {min(list1)}')
print(f'Maximum: {max(list1)}')
print(f'Length: {len(list1)}')
print(f'Sum: {sum(list1)}')
print(f'Average: {sum(list1) / len(list1)}')
print(f'Set: {set(list1)}')
print(f'Sorted in ascending order: {sorted(list1)}')
print(f'Sorted in descending order: {sorted(list1, reverse=True)}')



# Editing lists

lst = [1, 2, 3]

# append function to add a single value to the list
lst.append(4)
print(f'Append: {lst}')

# extend function to add another list to the existing list
lst.extend([5, 6, 8])
print(f'Extend: {lst}')

# insert function to add a value at a certain index
lst.insert(6, 7)
print(f'Insert: {lst}')

# remove function to remove a specified value
lst.remove(5)
print(f'Remove 5: {lst}')

# count function to count how many times a specified value occurs in a list
counts = lst.count(2)
print(f'Count of 2: {counts}')

# sort and sort reverse=True
print(f'Ascending: {sorted(lst)}')
print(f'Descending: {sorted(lst, reverse=True)}')

# copy function
copy_lst = lst.copy()
print(f'Copied list: {copy_lst}')

# pop function for retrieving and removing the first, last, or specified index value from a list
print(f'Front Pop: {lst.pop(0)}')
print(f'Back Pop: {lst.pop()}')
print(f'New lst: {lst}')


# filter and map functions
#filter function to return the even numbers from lst
if __name__ == "__main__":
    def even_num(number):
        if number % 2 == 0:
            return True
        return False

even_lst_iterator = filter(even_num, lst)

even_lst = list(even_lst_iterator)
print(even_lst)

#map function to return the cuberoot 
if __name__ == "__main__":
    def cube_root(number):
        return np.cbrt(number)

cube = map(cube_root,lst)
print(f'Map lst: {list(cube)}')

# map function to return the volume of cubes

def vol(side):
    return side ** 3

vol_lst = map(vol, lst)
print(f'Volumes: {list(vol_lst)}')


# list comprehension
# filtering a list using comprehension
print(f'list1: {list1}')
list2 = [x for x in list1 if x<15]
print(f'list2: {list2}')

#comprehension to triple each value in list1
triple_lst = [x * 3 for x in list1]
print(f'triple_lst: {triple_lst}')
# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("your code here")


# Why? Why only print if this the module called?
# Because when you write good functions, you may want to
# import this module into another script - just like you did
# math or statistics.
# Build a library of resuable functions to support your domain.

# For example, if your domain:
# Is sports, create functions to provide a list of teams.
# Is pets, create functions to calculate adoption prices.
# Is music, create functions to return a list of your favorite artists.


# When you write reusable functions for your domain, you can
# import the module with your utility functions into other modules
# and use them there.  This is a very common practice.
# Anything you write can be imported into later projects.

