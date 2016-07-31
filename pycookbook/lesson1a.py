# List filtering
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
greater_than_zero=[n for n in mylist if n > 0] #Filtering at source
zero_or_positive=[n if n > 0 else 0 for n in mylist] #Clipping and NO Filter
generator_from_list=(n for n in mylist if n > 0) #Filtered returning iterator
