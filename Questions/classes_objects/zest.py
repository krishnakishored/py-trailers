class Pair:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r},{0.y!r})'.format(self)
    
    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)

        

# if __name__=="__main__":
'''
Every module in python has a special attribute called __name__ . 
The value of __name__  attribute is set to '__main__'  when module run as main program. 
Otherwise the value of __name__  is set to contain the name of the module.
'''