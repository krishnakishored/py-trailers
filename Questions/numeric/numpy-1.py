# https://www.python-course.eu/numpy.php

import numpy as np


from sys import getsizeof as size # calculate the memory consumption of the list



cvalues = [20.1, 20.8, 21.9, 22.5, 22.7, 22.3, 21.8, 21.2, 20.9, 20.1]


#size comparison
def test_numpy_vs_list_1():
    # We will turn our list "cvalues" into a one-dimensional numpy array:   
    C = np.array(cvalues) # C is an instance of the class numpy.ndarray"
    print(C)
    print(C * 9 / 5 + 32)
    print(C) #array C has not been changed by this expression:
    
    fvalues = [ x*9/5 + 32 for x in cvalues]
    print(fvalues)
    print(type(C)) # <class 'numpy.ndarray'>
    print(type(fvalues)) # <class 'list'>

    # import matplotlib.pyplot as plt
    # plt.plot(C)
    # plt.show()

    lst = [24, 12, 57]
    
    size_of_list_object = size(lst)   # only green box(list object)
    size_of_elements = len(lst) * size(lst[0]) # 24, 12, 57
    total_list_size = size_of_list_object + size_of_elements

    print("Size without the size of the elements: ", size_of_list_object) #88
    print("Size of all the elements: ", size_of_elements) #84
    print("Total size of list, including elements: ", total_list_size) #172 

    # Add a new element
    lst = [24, 12, 57, 42]
    size_of_list_object = size(lst)   # only green box
    size_of_elements = len(lst) * size(lst[0]) # 24, 12, 57, 42
    total_list_size = size_of_list_object + size_of_elements
    print("Size without the size of the elements: ", size_of_list_object)
    print("Size of all the elements: ", size_of_elements)
    print("Total size of list, including elements: ", total_list_size)
    
    lst = []
    print("Emtpy list size: ", size(lst))

    a = np.array([24, 12, 57])
    print(size(a))
    e = np.array([])
    print(size(e))

    # numpy automatically chooses a fixed integer size. - 3, 6, 12, 24
    a = np.array([24, 12, 57], np.int8)
    print(size(a) - 96)
    a = np.array([24, 12, 57], np.int16)
    print(size(a) - 96)
    a = np.array([24, 12, 57], np.int32)
    print(size(a) - 96)
    a = np.array([24, 12, 57], np.int64)
    print(size(a) - 96)


import time
size_of_vec = 1000
def pure_python_version_1():
    t1 = time.time()
    X = range(size_of_vec)
    Y = range(size_of_vec)
    Z = [X[i] + Y[i] for i in range(len(X)) ]
    return time.time() - t1
    
def numpy_version_1():
    t1 = time.time()
    X = np.arange(size_of_vec)
    Y = np.arange(size_of_vec)
    Z = X + Y
    return time.time() - t1



#time comparison
def test_numpy_vs_list_2():
    t1 = pure_python_version_1()
    t2 = numpy_version_1()
    print(t1, t2)
    print("Numpy is in this example " + str(t1/t2) + " faster!")





#time comparison using timeit
from timeit import Timer
def pure_python_version():
    Z = [X_list[i] + Y_list[i] for i in range(len(X_list)) ]

def numpy_version():
    Z = X + Y





if __name__ == "__main__":
    # test_numpy_vs_list_1()
    # test_numpy_vs_list_2()
    
    size_of_vec = 1000
    X_list = range(size_of_vec)
    Y_list = range(size_of_vec)
    X = np.arange(size_of_vec)
    Y = np.arange(size_of_vec)

    #timer_obj = Timer("x = x + 1", "x = 0")
    timer_obj1 = Timer("pure_python_version()", 
                   "from __main__ import pure_python_version")
    timer_obj2 = Timer("numpy_version()", 
                   "from __main__ import numpy_version")
    print(timer_obj1.timeit(10))
    print(timer_obj2.timeit(10))
    # The repeat() method is a convenience to call timeit() multiple times and return a list of results:
    print(timer_obj1.repeat(repeat=3, number=10))
    print(timer_obj2.repeat(repeat=3, number=10))




