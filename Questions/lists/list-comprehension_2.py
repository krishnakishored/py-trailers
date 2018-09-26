Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = [ ((float(9)/5)*x + 32) for x in Celsius ]
print(Fahrenheit)

# https://www.python-course.eu/python3_list_comprehension.php


# A Pythagorean triple consists of three positive integers a, b, and c, such that  a2 + b2 = c2. 

triplet = [(x,y,z)  for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2]
# triplet = [(x,y,z)  for x in range(1,30) for y in range(1,30) for z in range(1,30) if x**2 + y**2 == z**2]
print(triplet)

#Cross Product - A×B = {(a, b) : a belongs to A, b belongs to B}. 

colours = [ "red", "green", "yellow", "blue" ]
things = [ "house", "car", "tree" ]
coloured_things = [ (x,y) for x in colours for y in things ]
print(coloured_things)

# Generator Comprehension
# They are simply like a list comprehension but with parentheses - instead of (square) brackets around it. 
# Otherwise, the syntax and the way of working is like list comprehension, but a generator comprehension returns a generator instead of a list.
Fahrenheit_gen = (((float(9)/5)*x + 32) for x in Celsius )
print(Fahrenheit_gen)
print(list(Fahrenheit_gen))
# print(list(Fahrenheit_gen))# []
# print(tuple(Fahrenheit_gen))
print(type(Fahrenheit)) # <class 'list'>
print(type(Fahrenheit_gen)) # <class 'generator'>

x = (x**3 for x in range(10))
print(x) #<generator object <genexpr> at 0x10c4a3840>
for i in x:
    print(i, end=" ")
print("\n")

y = (y**2 for y in range(9))
y = list(y)
print(y)