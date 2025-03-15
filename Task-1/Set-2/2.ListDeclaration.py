list = [1, 2, 3, 4, 5]
Mixed_List = [1, "Hello", 3.4, True]
print(f"{list}")
print(f"{Mixed_List[1]}")
print(f"{Mixed_List}")

#

my_list = [1, 2, 3]

# Adding elements
my_list.append(4)  
# [1, 2, 3, 4]
my_list.insert(1, 100)  
# [1, 100, 2, 3, 4]

# Removing elements
my_list.remove(2)  
# Removes first occurrence of 2 
# [1, 100, 3, 4]

popped_item = my_list.pop()  
# Removes last element
# [1, 100, 3]

# Sorting
my_list.sort()  
# Sorts in ascending order
# [1, 3, 100]

# Reversing
my_list.reverse()  
# Reverses the order of elements
# [100, 3, 1]

print(my_list)