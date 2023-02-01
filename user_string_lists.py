"""
Kellie Heckman 31JAN23

"""

# imports first

import math
import random
import statistics as stats
import numpy as np

# reusable functions next

feed = ['corn', 'grains', 'pellet', 'crumble'] 
feed2 = ['insects', 'free_range', 'scraps']

species = ['brahma', 'cochin', 'australorp', 'polish']
species2 = ['wyandotte', 'faverolle', 'easter_egger']

#len and set
len_feed2 = len(feed2)
print(len_feed2) 

print(set(feed))

#zip function
zipped_species = zip(species, species2)
print(f'Zipped Species: {zipped_species}')

#random choice
random_species = random.choice(species)
print(f'The best chicken for you: {random_species}')







# call functions and execute code
# use if __name__ == "__main__":
