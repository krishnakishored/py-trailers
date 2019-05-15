#  https://www.python-course.eu/python3_object_oriented_programming.php
#  https://www.python-course.eu/python3_class_and_instance_attributes.php

class Robot:
    pass
'''
Binding attributes to objects is a general concept in Python. 
Even function names can be attributed. You can bind an attribute to a function name in the same way 
'''
def g(x):
    return 42

'''
This can be used as a replacement for the static function variables of C and C++, 
which are not possible in Python. We use a counter attribute in the following example: 

'''

def f(x):
    f.counter = getattr(f, "counter", 0) + 1 
    return "Monty Python"

if __name__ == "__main__":
    x = Robot()
    y = Robot()
    y2 = y
    print(y == y2) #True,  y2 is an alias name for y
    print(y == x)  #False

    # We can dynamically create arbitrary new attributes for existing instances of a class. 
    # We do this by joining an arbitrary name to the instance name, separated by a dot "."

    x.name= "Marvin"
    x.build_year = "1979"
    print(x.name)

    y.build_year = "1993"
    print(y.build_year)
    print(x.__dict__) # {'name': 'Marvin', 'build_year': '1979'}
    print(y.__dict__)
    print(y2.__dict__)
    Robot.brand = "Thales"
    x.brand="HTS"
    print(Robot.__dict__)
    # {'__module__': '__main__', '__dict__': <attribute '__dict__' of 'Robot' objects>, '__weakref__': <attribute '__weakref__' of 'Robot' objects>, '__doc__': None, 'brand': 'Thales'}
    print(y.brand) # Thales

    # If you try to access y.brand, Python checks first, if "brand" is a key of the y.__dict__ dictionary. 
    # If it is not, Python checks, if "brand" is a key of the Robot.__dict__. 
    # If so, the value can be retrieved. Else an attribute error is raised

    print(x.brand) # HTS

    # By using the function getattr, you can prevent this exception, if you provide a default value as the third argument:
    print(getattr(x,'energy',"not an attribute"))
    x.energy="high"
    print(getattr(x,'energy',"not an attribute")) # high
    
    g.x=43
    print(g(1))  # 42
    print(g.x) # 43

    for i in range(10):
        f(i)
    print(f.counter) # 10
    f(0)
    f(100)
    print(f.counter) # 12 - the no.of times the function is calleds