#The type() function is mostly used for debugging purposes. Two different types of arguments can be passed to type() function, single and three arguments. If a single argument type(obj) is passed, it returns the type of the given object. If three argument types (object, bases, dict) are passed, it returns a new type object. 


num1 = 10
num2 = 10.2
str = "name"
list = [1, 2, 3]
dict = {"name": "John", "age": 23}
tuple = (1, 2, 3)


print(type(num1))
print(type(num2))
print(type(str)) 
print(type(list))
print(type(dict))
print(type(tuple))