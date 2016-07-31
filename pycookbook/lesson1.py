#Dictionaries
d = {
        'a' : [1,2,3,4,5], 'b': [4,5,3,4,6] #simple way to program
    }
from collections import defaultdict, OrderedDict
d=defaultdict(list) #or use set instead of list
d['a'].append(1) #add element by element.
d['b'].append(4)
print(d)
d2=OrderedDict() #ordered as per insertion order
d2['foo'] = 1; d2['bar'] = 2; d2['spam'] = 3; d2['groak'] = 4; d2['gamma'] = 5;
print(d2)

# for Dict Calculations
prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}
minkey = min(prices) #default reference is with keys
min_price = min(zip(prices.values(), prices.keys())) # create a Tuple to do the ordering in right order
max_price = max(zip(prices.values(), prices.keys()))
prices_orted = sorted(zip(prices.values(), prices.keys()))

# commonalities
a = {'x' : 1, 'y' : 2, 'z' : 3 }
b = { 'w' : 10, 'x' : 11, 'y' : 2 }
a.keys() & b.keys() # Common keys in dict
a.keys() - b.keys() # subset of keys
a.items() - b.items() # comparing the values instead of keys

# remove duplicates without changing Order 
# This also has mapping function - key
def dedupe(items, key=None):
    seen=set()
    for item in items:
        val = item if key is None else key(item) #Watch the if expression !
        if val not in seen:
            yield item
            seen.add(val)
a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))

# Slice of list (string is also a list)
#Useful for flat file record building
lam=np.random.random_integers(100) #lambda for poisson distribution
a=np.random.poisson(lam, size=15) #array([75, 67, 70, 66, 60, 72, 55, 70, 63, 65, 67, 73, 67, 64, 62])
s=slice(5,10) #Slice function to build specs
print(a[s]) #Slice of array

# most frequently occuring items in list
words = [
       'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
       'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
       'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
       'my', 'eyes', "you're", 'under' ]
morewords = ['why','are','you','not','looking','in','my','eyes']
from collections import Counter
word_count=Counter(words) #intelligent Dictionary
more_count=Counter(morewords)
top3 = word_count.most_common(3)
print(top3)
print(word_count['into'])
print(word_count + more_count) #Adds the elementwise counts!!

# Sorting a List of Dictionaries by a Common Key
# Using operator package
# Use itemgetter for items in dict and attrgetter in class objects
rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
from operator import itemgetter, attrgetter 
rows_by_fname=sorted(rows, key=itemgetter('fname')) # Same thing can be achieved using lambda expression as well
rows_by_lname = sorted(rows, key=itemgetter('lname'))
rows_by_lname_and_fnae=sorted(rows, key=itemgetter('lname', 'fname'))

# Grouping Records Together Based on a Field
rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
from itertools import groupby
rows=sorted(rows,key=itemgetter('date')) #Sort the list - only works with sorted list
g=groupby(rows, key=itemgetter('date')) #Watch that iterator is not consumed
for date, items in g:
    print(date)
    for i in items:
        print(' ', i)




pass

