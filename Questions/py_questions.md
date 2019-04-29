```Python general questions```
------------------------------
1) what is the difference between python and other laungages ??
2) Mention few benefits of using Python?
3) Does Python allow arguments Pass by Value or Pass by Reference?
4) Why is the “pass” keyword used for in Python?
5) Why is <__init__.py> module used for?
6) Differentiate between .py and .pyc files?
7) Explain how Python does Compile-time and Run-time code checking?
8) How memory is managed in Python?
9) what is the use of setup.py in python
10) what is the use of __init__==__main__: condition in python??
11) what is the type of *args and **kargs ??
12) difference between %s and %r in python
13) What is module and package in Python?
14) How will you set a global variable inside a function?
15) How will you share global variables across modules?
16) What are the tools that help to find bugs or perform static analysis?
17) As Everything in Python is an Object, Explain the characteristics of Python's Objects.
18) Diff between __repr__ and ___str___ methods
19) Are there equivalents to pointers & references in C/C++
20) How do create an executable with .py files
21) use of __name__=="__main__"
22) @property
23) recursive functions 
24) Memoization 
      * https://www.python-course.eu/python3_memoization.php
      > Memoisation is a technique used in computing to speed up programs. This is accomplished by memorizing the calculation results of processed input such as the results of function calls.French Jesuit Claude-Gaspar Bachet phrased it.

25) logging module
      * https://pymotw.com/3/logging/index.html#module-logging

Python string questions:-
--------------------------
1) What is slicing in Python? Explain with example.
2) What is a negative index in Python?
3) What is the best way to split a string in Python?
4) What is the right way to transform a Python string into a list?
5) How will you convert a string to a number in Python?


Python library functions
--------------------------

python iterators related questions:-
-------------------------------------
1) What are iterators in Python?
2) What are generators in Python? and yield keyword use in python ??
3) list comprehensions in python ??
   * https://www.digitalocean.com/community/tutorials/understanding-list-comprehensions-in-python-3
   > List comprehension is an elegant way to define and create list in Python
     list_variable = [x for x in iterable]
    
4) zip function in python ??
5) What is the use of enumerate() in Python?
6) lamda expressions in python ???
7) Map,reduce and filter functions in python ???

      s> The map() built-in function is another “iterator operator” that, in its simplest form, applies a single-parameter function to each element of an iterable one element at a time:


8) What is the difference between Xrange and range?
9) Difference between iterable and iterator
     https://stackoverflow.com/questions/9884132/what-exactly-are-iterator-iterable-and-iteration
    
    > In Python, iterable and iterator have specific meanings.
    An iterable is an object that has an __iter__ method which returns an iterator, or which defines a __getitem__ method that can take sequential indexes starting from zero (and raises an IndexError when the indexes are no longer valid). So an iterable is an object that you can get an iterator from.
    - Iterables can return their elements one at time.
    - Technically, any Python object that implements the .__iter__() or .__getitem__() methods is iterable.
    - The iter() built-in function, when called on an iterable, returns an iterator object for that iterable:

    > An iterator is an object with a next (Python 2) or __next__ (Python 3) method.
    Whenever you use a for loop, or map, or a list comprehension, etc. in Python, the next method is called automatically to get each item from the iterator, thus going through the process of iteration.
    
    > The Python itertools module is a collection of tools for handling iterators. Simply put, iterators are data types that can be used in a for loop. The most common iterator in Python is the list


    > Iterators are themselves also iterable, with the distinction that their __iter__() method returns the same object (self), regardless of whether or not its items have been consumed by previous calls to next().

    Quiz: Do you see how...
    - every iterator is an iterable?
    - a container object's __iter__() method can be implemented as a generator?
    - an iterable plus a __next__ method is not necessarily an iterator?
    
10) Set comprehension
      > A set comprehension is similar to a list comprehension, but returns a set and not a list. Syntactically, we use curly brackets instead of square brackets to create a set.

11) what are itertools?
      > https://realpython.com/python-itertools/

Python mechanism related questions:-
------------------------------------
1) Explain the use of with statement?  (python context manager mechanism)
      > Locks implement the context manager API and are compatible with the with statement. Using with removes the need to explicitly acquire and release the lock.

      
2) Whenever Python exists Why does all the memory is not de-allocated / freed
   (python garbage collector mechanism when Python exits?)
3) Explain about Python decorators?
      > A decorator in Python is any callable Python object that is used to modify a function or a class. Decorator is simply a callable object that takes a function as an input parameter
      > Decorators can take arguments. We redefine our decorator.The outermost function takes the arguments,the next more inner function takes the function and the innermost function will be returned and will replace the original function
4) What is Pickling and how does it different from Unpickling?
5) Decorators used for Polynomial functions in Python
      * https://www.python-course.eu/polynomial_class_in_python.php
6) Callable objects of Python
      > A callable object is an object which can be used and behaves like a function but might not be a function. It is possible to define classes in a way that the instances will be callable objects. The __call__ method is called, if the instance is called "like a function", 
7)  write a fibonacci class using __call__
8) Closures 
      > The local function is able to reference the outer scope through closures. Closures maintain references to objects from the earlier scope.   
      Closure is commonly used in what is referred to as Function Factory - these are functions that return other functions. 
      a closure is a combination of code and scope.  a closure is a function (object) that remembers its creation environment (enclosing scope).
      A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory
9) Global & non-local
      > global is a python keyword that introduces names from global namespace into the local namespace.
      The nonlocal keyword allows us to introduce names from enclosing namespace into the local namespace. 

File realted questions:-
-------------------------
1) How do you check the file existence and their types in Python?
2) How do you open a file in python?? and why??
3) How do you check list of files in the given path in python ??
4) How do you check whether file is exist or not in python
5) How do you perform copy file cmd in python ??
6) Explain how to delete a file in Python?


Collections(list,tuple,set,dictionary):-
-----------------------------------------
1) When to use list ?? tuple ?? set ?? and dictionary in python ??
2) List out the each collections(list,tuple,set and dictinary)object type. i.e
   List which are mutable objects and which are immutable objects ??
   * https://www.programiz.com/python-programming/list

3) How will you remove the duplicate elements from the given list?
4) What is the best approach to store a list of an employee’s first and last names?
5) Why don't we use list as dictionary key??


```OOPS```
--------------
1) Is Python object oriented? what is object oriented programming?
2) java type constructor in python??
3) self keyword use in python??
4) Explain Inheritance in Python with an example.
5) Explain polymorphism in python with an static binding and dynamic binding examples ??
6) Method overriding???
7) How instance variables are different from class variables?
8) Can you write code to check whether the given object belongs to a class or its subclass?
9) Abstract class implementation in python ?? can we create object for abstract class ?? if not then how we can call the abstract class members??
10) Super keyword use in python oops concept??
11) Could you please explain MRO(Method resolution order) in python ??
12) Compostion vs inheritance vs aggregation ??
13) Static variables and static methods in python ??
14) Does diamond probelm exist in python ??
15) Does python support multiinheritance ??
16) Does Python supports interfaces like in Java? Discuss.
17) Name and explain the three magic methods of Python that are used in the construction and initialization of custom Objects.
18) What are the different methods Python provides for copying an object?
19) How to prevent class 'a' from being inherited by another class?
    and also how to prevent parent class method 'm' from being inherited by another class?
20) How do you implement constant variables in python ???
21) Exact use of Abstract class??
22) Is there object slicing in Python
23) Magic Methods and Operator Overloading
      * https://www.python-course.eu/python3_magic_methods.php     





Exception Handling:-
-----------------------

1) What is an exception?
2) What are Exception Handling? How do you achieve it in Python?
3) Explain different ways to trigger / raise exceptions in your python script ?
4) How many except statements can a try-except block have??
5) When will the else part of try-except-else be executed?
6) When is the finally block executed?
7) Is it necessary that each try block must be followed by a except       block?
8) Can finally block be used without except?
9) Is there any case when finally will not be executed?
10) what happened return statement is in except block
11) will finally run after return??
12) How do you implement custom exception in python ??

Threading :-
--------------
1) What is the difference between Process and Thread?
> Using threads allows a program to run multiple operations concurrently in the same process space.


2) What are the benefits of multi-threaded programming?
3) What is difference between user Thread and daemon Thread?
4) What are the libraries in Python that support threads?
5) difference between sleep() and wait() method ???
6) join() method use in python ??
7) What is synchronization3 0
8) Explain about Lock ?? and its two states(acquire and release??
9) What is Deadlock? How to analyze and avoid deadlock situation?
10) Explain about wait(),notify() and notifyALL() methods ??
      (Inter process communication methods)
      (Thread condition mechanism)
      * https://pymotw.com/3/threading/#thread-objects
      
11) Why wait(), notify() and notifyAll() methods have to be called from
      synchronized method or block?
12) What is the difference between threading.Lock and threading.RLock?
13) When and how to use Python's RLock??
14) How to terminate a blocking thread?
15) Can we start a thread twice ??
16) Subclassing threads

Handling JSON
--------------

.... 

Numpy & Pandas
--------------
- Hinton diagram. The size of a square within this diagram corresponds to the size of the value of the depicted matrix. The colour determines, if the value is positive or negative. 

- The main benefits of using numpy arrays should be smaller memory consumption and better runtime behaviour.

- `matplotlib.pyplot`
- `getsizeof` -  for every new element, we need another eight bytes for the reference to the new object. The new integer object itself consumes 28 bytes. 
      The size of a list "lst" without the size of the elements can be calculated with: 64 + 8 * len(lst)

      That an arbitrary integer array of length "n" in numpy needs: 96 + n * 8 Bytes
      whereas a list of integers needs: 64 + 8 * len(lst) + len(lst) * 28


- `time.time()`, `timeit`, `repeat()`
- `dot(a, b, out=None)` - equivalent to matrix multiplication
- There are "real" matrices in Numpy. They are a subset of the two-dimensional arrays. We can turn a two-dimensional array into a matrix by applying the "mat" function. The main difference is if you multiply two two-dimensional arrays or two matrices,  we get real matrix multiplication by multiplying two matrices, but the two-dimensional arrays will be only multiplied component-wise.
-  If we compare two arrays, we don't get a simple True or False as a return value. The comparisons are performed elementswise. This means that we get a Boolean array as a return value.
- `array_equal` returns True if two arrays have the same shape and elements, otherwise False will be returned.
- Broadcasting, which allows to perform arithmetic operations on arrays of different shapes.  Under certain conditions, the smaller array is "broadcasted" in a way that it has the same shape as the larger array.





Bokeh
--------------



Flask
--------------

1. what are microservices
2. data migration
3. Flask & NodeJs - comparision



``` Questions from Cookbook```


interview questions - bogotobogo
--------------------------------

1. List of codes for interview Q & A
2. Merging two sorted list
3. Get word frequency - initializing dictionary
4. Initializing dictionary with list
5. map, filter, and reduce
6. Write a function f() - yield
7. What is __init__.py?
8. Build a string with the numbers from 0 to 100, "0123456789101112..."
9. Basic file processing: Printing contents of a file - "with open"
10. How can we get home directory using '~' in Python?
11. The usage of os.path.dirname() & os.path.basename() - os.path
12. Default Libraries
13. range vs xrange
14. Iterators
15. Generators
16. Manipulating functions as first-class objects
17. docstrings vs comments
18. using lambdda
19. classmethod vs staticmethod
20. Making a list with unique element from a list with duplicate elements
21. *args and **kwargs
22. mutable vs immutable
23. Difference between remove, del and pop on lists
24. Join with new line
25. Hamming distance
26. Floor operation on integers
27. Fetching every other item in the list
28. Python type() - function
29. Dictionary Comprehension
30. Sum
31. Truncating division
32. Differences Python 2 vs Python 3
33. len(set)
34. Print a list of file in a directory
35. Count occurrence of a character in a Python string
36. Make a prime number list from (1,100)
37. Reversing a string - Recursive
38. Reversing a string - Iterative
39. Output?
40. Merging overlapped range
41. Conditional expressions (ternary operator)
42. Function args
43. Unpacking args
44. Finding the 1st revision with a bug
45. Which one has higher precedence in Python? - NOT, AND , OR
46. Decorator(@) - with dollar sign($)
47. Multi-line coding
48. Recursive binary search
49. Iterative binary search
50. Pass by reference
51. Simple calculator
52. iterator class that returns network interfaces
53. Converting domain to ip
54. How to count the number of instances
55. Python profilers - cProfile
56. Calling a base class method from a child class that overrides it
57. How do we find the current module name?
58. Why did changing list 'newL' also change list 'L'?
59. Construction dictionary - {key:[]}
60. Colon separated sequence
61. Converting binary to integer
62. 9+99+999+9999+...
63. Calculating balance
64. Regular expression - findall
65. Chickens and pigs
66. Highest possible product
67. Copy an object
68. Products
69. Pickle
70. Overlapped Rectangles
71. \__dict__
72. Fibonacci I - iterative, recursive, and via generator
73. Fibonacci II - which method?
74. Stack with returning Max item at const time
75. Finding duplicate integers from a list - 1
76. Finding duplicate integers from a list - 2
77. Finding duplicate integers from a list - 3
78. Reversing words 1
79. Parenthesis, a lot of them
80. Palindrome / Permutations
81. Constructing new string after removing white spaces
82. Removing duplicate list items
83. Dictionary exercise
84. printing numbers in Z-shape
85. Factorial
86. lambda, lambda with map/filter/reduce
87. Number of integer pairs whose difference is K
88. Recursive printing files in a given directory
89. Bubble sort
90. What is GIL (Global Interpreter Lock)?
91. Word count using collections
92. Pig Latin
93. List of anagrams from a list of words
94. Write a code sending an email using gmail
95. histogram 1 : the frequency of characters
96. histogram 2 : the frequency of ip-address
97. Creating a dictionary using tuples
98. Getting the index from a list
99. Looping through two lists side by side
100. Dictionary sort with two keys : primary / secondary keys
101. Writing a file downloaded from the web
102. Sorting csv data
103. Reading json file
104. Sorting class objects
105. Parsing Brackets
106. Printing full path
107. str() vs repr()
108. Missing integer from a sequence
109. Polymorphism
110. Product of every integer except the integer at that index
111. What are accessors, mutators, and @property?
112. N-th to last element in a linked list
113. Implementing linked list
114. Removing duplicate element from a list
115. List comprehension
116. .py vs .pyc
117. Binary Tree
118. Print 'c' N-times without a loop
119. Quicksort
120. Dictionary of list
121. Creating r x c matrix
122. str.isalpha() & str.isdigit()
123. Regular expression
124. What is Hashable? Immutable?
125. Convert a list to a string
126. Convert a list to a dictionary
127. List - append vs extend vs concatenate
128. Use sorted(list) to keep the original liste
129. list.count()
130. zip(list,list) - weighted average with two lists
131. Intersection of two lists
132. Dictionary sort by value
133. Counting the number of characters of a file as One-Liner
134. Find Armstrong numbers from 100-999
135. Find GCF (Greatest common divisor)
136. Find LCM (Least common multiple)
137. Draws 5 cards from a shuffled deck
138. Dictionary order by value or by key
139. Regular expression - password check
140. Prime factors : n = products of prime numbers
141. Valid IPv4 address
142. Sum of strings
143. List rotation - left/right
144. shallow/deep copy
145. Converting integer to binary number
146. Creating a directory and a file
147. Creating a file if not exists
148. Invoking a python file from another


