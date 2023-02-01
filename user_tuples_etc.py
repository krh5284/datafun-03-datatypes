"""
Kellie Heckman 31JAN23

"""
#tuples
layers_id = (1, 2, 3, 4, 5)
meaters_id = (4, 5, 6, 7, 8)
total = layers_id + meaters_id
print(f'All chicken ID numbers: {total}')


#Sets
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

# set union
setC = setA | setB
print(f'Union: {setC}')

# set intersection
setD = setA & setB
print(f'Intersection: {setD}')