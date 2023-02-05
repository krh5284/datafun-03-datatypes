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



# Dictionaries


with open("text_woodchuck.txt") as file_object:
    word_list = file_object.read().split()

word_count = {word: word_list.count(word) for word in word_list}


print(f'Word count:  {word_count}')

word_list_lower = [x.lower() for x in word_list] # change to lowercase
word_list_mod = [str.replace(",", "") for str in word_list_lower] # remove ,
word_list_mod2 = [str.replace("?", "") for str in word_list_mod] # remove ?
word_list_mod3 = [str.replace(".", "") for str in word_list_mod2] # remove .

word_count = {word: word_list_mod3.count(word) for word in word_list_mod3}
print(f'Word count mod:  {word_count}')
