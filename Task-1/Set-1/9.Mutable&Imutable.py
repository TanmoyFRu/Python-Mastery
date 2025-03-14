# For String

string = "Hello World"
# ==> string[4] = "s"
print(string)
# In the code snippet, the string is defined as "Hello World". The value at the index 4 is changed to "s". However, strings are immutable, and you cannot change the value of an element in a string. Therefore, the code will raise an error. 

# For Tuple

tuple= (1, 2, 3, 4, 5)
# ==> tuple[4] = 6
print(tuple)
# In the code snippet, the tuple is defined with the values (1, 2, 3, 4, 5). The value at the index 4 is changed to 6. However, tuples are immutable, and you cannot change the value of an element in a tuple. Therefore, the code will raise an error.

# For List

list = [1, 2, 3, 4, 5]
list.append(6)
print(list)
# In the code snippet, the list is defined with the values [1, 2, 3, 4, 5]. The append() method is used to add the value 6 to the end of the list. The output will be [1, 2, 3, 4, 5, 6].

list = [1, 2, 3, 4, 5]
list.insert(2, 6)
print(list)
# In the code snippet, the list is defined with the values [1, 2, 3, 4, 5]. The insert() method is used to insert the value 6 at index 2. The output will be [1, 2, 6, 3, 4, 5].

# For Dictionary

dir = {"Name": "tanmoy", "Age": 22}
dir["Age"] = 23
print(dir)
# In the code snippet, the list is defined with the values [1, 2, 3, 4, 5]. The append() method is used to add the value 6 to the end of the list. The output will be [1, 2, 3, 4, 5, 6].