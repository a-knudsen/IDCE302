# Tuples
## pronounced two-ples

## review dictionaries:
- .keys() returns the key 
- .values() returns the value for each key
- .items() returns all items in the dictionary as a list
- .clear() clears the dictionary 
--------------------------------------
- similr to lists but **immutable**
- good for datasets that you don't want to change
- methods such as sort and reserve don't work
- syntax: tuple = ('a', 'b', 'c', 'd')
- retrieving items:
    - if I want a: index[0]
    - if I want b and c: index [1:3] because includes up to but not 3
    
- can use **zip** function to combine strings and lists to get tuples


class demo review of dictionary exercise:

#class 10-3
#review on dictionaries

legend = {0:'novalue', 1:'deciduous', 2:'conifers', 3: 'industrial', 4:'residential', 5:'water bodies', 6:'agricultural'}

def printdict (dictionaryname):
  for i in dictionaryname:
    return dictionaryname.items()

print printdict(legend)
# print legend.values()

#shadrock's answer, looks nicer
def printDict (dictinput):
  for (key, value) in dictinput.items():
    print key, value
printDict(legend)
