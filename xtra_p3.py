"""
Optional bonus. See course site for details.

>>> len(longwordset1)
415

>>> len(longwordset2)
197

>>> len(longwords)
13
"""

import doctest

# Readh from two files to get a list of words for each

with open("text_hamlet.txt", "r") as f1:
    text = f1.read()
    wordlist1 = text.split()  # split on whitespace


with open("text_juliuscaesar.txt", "r") as f2:
    text = f2.read()
    wordlist2 = text.split()  # split on whitespace

# Removed duplicates by creating two sorted sets

wordset1 = set(sorted(wordlist1))  
wordset2 = set(sorted(wordlist2)) 


# created lists of words with more than 10 characters and then transformed to sets to remove duplciates

maxlen = 10 

longwordset1 = set(list(word for word in wordset1 if len(word) > maxlen))  # TODO: fix this line
longwordset2 = set(list(word for word in wordset2 if len(word) > maxlen))  # TODO: fix this line


# intersection of the two sets

longwords = longwordset1 & longwordset2

# length of the sets and the list
print(len(longwordset1))
print(len(longwordset2))
print(len(longwords))
print()
print(f"{sorted(longwords) = }")
print()

# check your work
print("TESTING...if nothing prints before the testing is done, you passed!")
doctest.testmod()
print("TESTING DONE")
