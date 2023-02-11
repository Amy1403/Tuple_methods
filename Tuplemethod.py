Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)

# index method
# ---------------------------------------
# first method
# getting the index of 3
res = Tuple.index(3)
print('First occurrence of 3 is', res)


# second method
# getting the index of 3 after 4th index
res = Tuple.index(3, 4)
print('First occurrence of 3 after 4th index is:', res)


# Creating a tuple of numbers
Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2, 6)


# Creating a tuple of strings
Tuple2 = ('python', 'geek', 'python', 
          'for', 'java', 'python')
  
# count method
# --------------------------------------------

# third method
# count the appearance of 3
res = Tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)


# fourth 
# count the appearance of python
res = Tuple2.count('python')
print('Count of Python in Tuple2 is:', res)


# fifth method
# find the index of the number of 3 between the third and seventh element
res = Tuple2.index('python', 3, 7)
print('Count of Python in Tuple2 is:', res)
