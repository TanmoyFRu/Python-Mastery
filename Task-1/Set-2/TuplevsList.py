my_list = [1, 2, 3]
my_list.append(4)  #* ✅ Can add elements
my_list[0] = 100   #* ✅ Can modify elements
print(my_list)  
# Output: [100, 2, 3, 4]


my_tuple = (1, 2, 3)
# my_tuple.append(4)  #! ERROR: Tuples don’t support appending
# my_tuple[0] = 100   #! ERROR: Tuples cannot be modified
print(my_tuple)  
# Output: (1, 2, 3)
