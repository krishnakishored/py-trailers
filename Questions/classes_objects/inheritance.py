# https://www.python-course.eu/python3_inheritance.php

class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    # def Name(self):
    #     return self.firstname + " " + self.lastname

    #  use __str__ method instead - a leaner design
    def __str__(self):
        return self.firstname + " " + self.lastname

class Employee(Person):
    '''
    The __init__ method of our Employee class explicitly invokes the __init__method of the Person class. We could have used super instead. 
    super().__init__(first, last) is automatically replaced by a call to the superclasses method, in this case __init__:
    '''

    def __init__(self, first, last, staffnum):
        # Person.__init__(self,first, last)
        super().__init__(first,last)
        self.staffnumber = staffnum

    # def GetEmployee(self):
    #     return self.Name() + ", " +  self.staffnumber

    def __str__(self):
        ''' overridden the method __str__ from Person in Employee. '''
        return super().__str__() + ", " +  self.staffnumber


# overloading can be simulated using default parameters or * operator
def f(*x):
    if len(x) == 1:
        return x[0] + 42
    else: 
        return x[0] + x[1] + 42


def f2(n, m=None):
    if m:
        return n + m +42
    else:
        return n + 42        

if __name__ == "__main__":
   
    x = Person("Marge", "Simpson")
    y = Employee("Homer", "Simpson", "1007") 

    # print(x.Name())
    # print(y.GetEmployee())

    print(x)
    print(y)

    print(f(43)) 
    print(f(43,100)) 
    

    print(f2(43)) 
    print(f2(43,100)) 
    