class Robot:
    pass


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
    print(y == y2) #True
    print(y == x)  #False

    x.name= "Marvin"
    x.build_year = "1979"
    print(x.name)

    y.build_year = "1993"
    print(y.build_year)
    print(x.__dict__)
    print(y.__dict__)
    print(y2.__dict__)
    Robot.brand = "Thales"
    x.brand="HTS"

    print(Robot.__dict__)
    print(y.brand)

    print(x.brand)
    print(getattr(x,'energy',"not an attribute"))
    x.energy="high"
    print(getattr(x,'energy',"not an attribute"))
    # print(x.energy)

    g.x=43
    print(g.x)

    for i in range(10):
        f(i)

    print(f.counter) # 10

#  https://www.python-course.eu/python3_object_oriented_programming.php