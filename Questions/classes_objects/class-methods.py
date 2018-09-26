class Robot:
    def __init__(self,name=None):
        # print("__init__ has been executed")
        self.name = name

    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")

    def set_name(self, name):
        self.name = name
        
    def get_name(self):
        return self.name   

    def set_build_year(self, by):
        self.build_year = by
        
    def get_build_year(self):
        return self.build_year    
     

if __name__=="__main__":
    x = Robot()
    # x.say_hi()
    # y= Robot("Marvin")
    # y.say_hi()
    x.set_name("Henry")
    x.say_hi()
    y = Robot()
    y.set_name(x.get_name())
    print(y.get_name())






'''
For a Class C, an instance x of C and a method m of C the following three method calls are equivalent:
type(x).m(x, ...)
C.m(x, ...)
x.m(...)

'''




















'''
We have seen that a method differs from a function only in two aspects:
It belongs to a class, and it is defined within a class
The first parameter in the definition of a method has to be a reference to the instance, which called the method. 
This parameter is usually called "self".


For a Class C, an instance x of C and a method m of C the following three method calls are equivalent:
type(x).m(x, ...)
C.m(x, ...)
x.m(...)


Data Abstraction = Data Encapsulation + Data Hiding 


'''

