#Logical operators
"""
Logical operators are: And, Or, Not
"""
#Example (And)

x = 10
y = 16
b = 1
c = 3

if y == x and b == c:
    print('same')
else: 
    print('Not same')

#Example (or)

x = 10
y = 16
b = 1
c = 3

if y == x or b == c:
    print('same')
else: 
    print('Not same')

#Example (not)

x = 10
y = 16
b = 1
c = 3

if not(y == x or b == c):
    print('same')
else: 
    print('Not same')