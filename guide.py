# 'is' VS '=='
# == determines if two obj have the same value
# is determines if two references refers to the same obj

#tuples VS list
# tuples cannot be modified. Used to represent a fixed collection of items
# list can be modified

#Tuples: cannot be modified
tuple = ("apple", "banana", "cherry")

#List: ordered, changeable, and allow duplicate values
list = ["notebook", "pencil", "eraser"]

#Arrays: used to store multiple values in one single var
#cars[0] = Ford
cars = ["Ford", "Volvo", "BMW"]

#Operators: perform operations on var and values
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 % 5)
print(10 ** 5)
print(10 // 5)

#Set: stores multiple items in a single var.
#unchangeable, but can remove items and add new items
set = {"burger", "fries", "cola"}

#Lambda: anonymous function
#multiplication
x = lambda a, b : a * b
print(x(5, 6))
