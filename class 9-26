# date: 9/26
## Topic: LISTS 

# lists are collections of many values called elements (strings, ints, floats)
# they are mutable (changeable)
# define with []
# '+' operation concatenates lists
# '*' operation repeats list a given number of times

#splitting lists:
>>> text = "thee akd alag akjhg"
>>> words = text.split()
>>> print (words)
['thee', 'akd', 'alag', 'akjhg']
>>> feats = ['pt', 'line', 'poly']
# can print everything in list
>>> print(feats)
['pt', 'line', 'poly']
>>> print('point' in feats)
False
>>> historylist = ['Mumbai', 'was', 'formerly', 'Bombay']
# .join() function: 
>>> myst = '_'.join(historylist)
>>> print(myst)
Mumbai_was_formerly_Bombay
>>> print (historylist)
['Mumbai', 'was', 'formerly', 'Bombay']
>>> myst = ' '.join(historylist)
>>> print(myst)
Mumbai was formerly Bombay
>>> 

# slicing a list with "[::-1]" produces a reversed copy 
# or can use .reverse() to reverse the actual order of the list
>>> cities = ["Jakarta", "Mumbai", "Nairobi"]
>>> print (cities[::-1])
['Nairobi', 'Mumbai', 'Jakarta']
>>> cities.reverse() #doing this changes the list itself 
>>> print(cities)
['Nairobi', 'Mumbai', 'Jakarta']
 
>>> # using indexing to change an element in a list
>>> numbers = [17, 89]
>>> print (numbers)
[17, 89]
numbers[0:1] = [89, 17] .... ??moving on

>>> #changing elements in a list
>>> lamelist = ['a', 'b', 'c', 'd']
>>> # want to change it to a, x, y, z
# colon starts at input (1) and stops right before second input (3) 
>>> lamelist[1:3] = ['x', 'y']
>>> print (lamelist)
['a', 'x', 'y', 'd']
>>> #inserting elements in a list
>>> letters = ['a', 'd', 'f']
>>> letters[1:1] = ['b', 'c']
>>> print(letters)
['a', 'b', 'c', 'd', 'f']
>>> #add in again 
>>> letters[4:4] = ['e']
>>> print (letters)
['a', 'b', 'c', 'd', 'e', 'f']
>>> #deleting elements, b and c
>>> letters[1:3] = []
>>> print (letters)
['a', 'd', 'e', 'f']
# can also use . del() operator 

##nested lists 


# side note, debugging
>>> def printDirections():
	directions = ['N', 'S', 'E', 'W']
	i=0
	while i<3:
		print(directions[i])
		i = i+1


>>> printDirections()
N
S
E
# index should have been while i< 4 to include all in list

#or can make a function to print list
>>> airports = ['DEN', 'LAX', 'BRU']
>>> def printList(listname):
	i=0
	while i< len(listname):
		print(listname[i])
		i= i+1
		
>>> printList(airports)
DEN
LAX
BRU
