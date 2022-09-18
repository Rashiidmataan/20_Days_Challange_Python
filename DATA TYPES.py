#Data types
"""
1. String
2. Integer
3. float
4. List
5. Tuple
6. Dictionary
7. Sets
8. bool
9. Casting
"""
# String Example


import string


x="axmed"
myString = str(x)
print(type(myString))


#Integer Example

x= 10
myInteger = int(x)
print(type(myInteger))

#Float Example
from msilib import MSIMODIFY_SEEK
from tkinter.font import names
from turtle import st
from typing import Dict


x=3.5
myFloat=float(x)
print(type(x))

#List example
x=(("abdi", "Yusut"))
myList=list(x)
print(type(myList))

#Tuple Example
names=("Sacdio", "Mane")
nyTuple=tuple(names)
print(type(names) )

#Dictionary Example
form={"Name:", "Sadio", "Age:", 30}
x= dict(Name="Sadio", Age=30)
myDic=dict(x)
print(type(x))

#sets Example
x= {"Canab", "Caruus", "Canbo"}
mySets=set(x)
print(type(x))