#First Method

num1 = 10
num2 = 20

print("Before swapping: num1 = ", num1, " num2 = ", num2)

num1, num2 = num2, num1

print("After swapping: num1 = ", num1, " num2 = ", num2)

#Second Method

num1 = 10
num2 = 20

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("After swapping: num1 = ", num1, " num2 = ", num2)