#Built-in Data types
"""
Variables can store data of different types, and different types can do different things.
"""
"""
Text Types - str
Numeric Types - int, float, complex
Sequence Types - list, tuple, range
Mapping Type - dict
Set Type - set, frozenset
Boolean Type - bool
Binary Types - bytes, bytearray, memoryview
None Type - NoneType
"""

#Getting the data type
x = 5
print(type(x))

#Setting the data type
x = "Hari" #str
x = 20 #int
x = 20.5 #float
x = 1j #complex
x = ["apple", "banana", "cherry"] #list
x = ("apple", "banana", "cherry") #tuple
x = range(2) #range
print(x)
x = {"name" : "John", "age" : 35} #dic
x = frozenset({"apple", "banana"}) #frozenset
print(x)
x = True #bool
x = b"Hari" #bytes
x = bytearray(5)
print(x)
x = None #NoneType
print(x)

#Setting the specific data type
x = str("Hari")
x = int(29)
x = float(2.4)
x = complex(1J)
x = list(("apple","banana"))
x = tuple(("apple","banana"))
x = range(4)
x = dict(name="John", age = 30)
x = set(("apple","banana"))
x = frozenset(("apple","banana"))
x = bool(4)
x = bytes(3)
x = bytearray(4)
x = memoryview(bytes(6)) #memoryview