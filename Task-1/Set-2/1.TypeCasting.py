#From a programming point of view, a type casting refers to converting an object of one type into another. Here, we shall learn about type casting in Python Programming

# Type Casting in Python

integer = 10
float = 10.5
print(f"{integer+float}")

#To perform their addition, 10 − the integer object is upgraded to 10.0. It is a float, but equivalent to its earlier numeric value. Now we can perform addition of two floats.

#a Boolean object is first upgraded to int and then to float, before the addition with a floating point object. In the following example, we try to add a Boolean object in a float, pleae note that True is equal to 1, and False is equal to 0.

IAmPoor = True # 1.0
print(f"{float+IAmPoor}")

#String to Int

#To convert a string to an integer, we use the int() function. The int() function takes in any data type and converts it into an integer. However, if the string is not a valid number, it will throw a ValueError.

string = "10"
print(f"{int(string)}")

#Float to Int

a = int(10.5)
print(a)

b = int("10.5")
print(b)