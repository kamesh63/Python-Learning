#creating variables
x = 5
y = "Hari"
print(x)
print(y)

#Casting 
x = str(3) # '3'
y = int(3) # 3
z = float(3) # 3.0

#Get the type
print(type(x))

#Case sensitive
a = 4
A = 4 #Both are different

#Rules for Creating variable names
"""
1.Must Start with a letter or the underscore character
2.Cannot start with a number
3.Only contain alpha-numeric and underscore (A-Z, 0-9, _)
4.Case sensitive(age,Age,AGE)
5.A Variable cannot be any of the python keywords.
"""

#Multi Words Variable Names
""" More than a word can be difficult to read. Several techniques to make them more readable """
#1.Camel case
myVariableName = "Hari"
#2.Pascal case
MyVariableName = "Hari"
#3.Snake case
my_variable_name = "Hari"

#Many values to multiple variables
a,b,c = "Orange", "Banana", "Cherry"

#One Value to multiple variables
d = e = f = "Orange"

#Unpack a Collection
""" 
If you have a collection of values in a list, tuple etc... Python allows you to extract the values into variables called unpacking
"""
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Global Variable
x = "Cool"
def myFunc():
  print("Python is " + x)
myFunc()

x = "Cool" #It should be global
def myFunc():
  x = "amazing"
  print("Python is " + x) #Calls local variable
myFunc()

#Global Keyword
""" We can create a variable inside the func using global keyword to call anywhere in the program """
def myFunc():
  global x
  x = "cool"
myFunc
print(x)

