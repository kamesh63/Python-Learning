#String 
"""
String in python are surrounded by either single quotation marks, or double quotation marks
'Hari' is the same as "Hari"
"""

#Quotes inside quotes
print("she is right")
print("she always 'right'")
print('she only "right"')

#Assigning str to variable
a = "Hari"
print(a)

#Multiline strings
a = """ Hari is cool,
OKKKKKKKKKKKKK""" 
print(a)

#Strings are arrays
"""
Strings in python are arrays of bytes representing unicode characters.
Python does not have a character data type, a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string.
"""
a = "Hello, Hari"
print(a[1]) #return position - 1

#Looping through a string
for x in "Hari":
  print(x)

#String Length
a = "Hari"
print(len(a)) #len() will be used

#Check String
"""
To check if a certain phrase or character is present in a string, we can use the keyword "in"
"""
txt = "The best things in life are free"
print("free" in txt) #returns bool value

#Check if not
txt = "The best things in life are free"
print("free" not in txt) #returns bool value... not in used

# ---------------------------------------------------------------------------------

#Slicing Strings
"""
we can return a range of characters by using the slice syntax
- Specify the start and end index, seperated by colon, to return a part of the string
"""
a = "Hari"
print(a[1:3]) #3 will be not included

#Slice from start
b = "Hari"
print(b[:3]) #Get the char from the start to position 3 (not include)

#Slice to the end
b = "Hari"
print(b[2:]) #Get the char from the start to position 2 ane all the way end

#Negative indexing
"""
index start from last to start
last 3 exludes
"""
b = "Hello, World!"
print(b[-5:-3])

#----------------------------------------------------------

