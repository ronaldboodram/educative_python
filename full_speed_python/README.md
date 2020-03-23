#Full Speed Python

#####Git
to use git from different computers, make use of ssh keys.  
1. Create or use existing ssh keys
2. Add ssh keys to your keychain: eg ssh-add ~./ssh/id_rsa
3. add the ssh key to github
4. clone and push to your remote repo

####Classes
A class contains a group of properties called attributes and functions.  Functions with in a 
class are called methods. **The methods are their to manipulate the properties in a class.**

An Object is an instance of a Class.

A constructor method is used to initialize the class's attributes. In the class the keyword self
is used to reference the attributes belonging to that instance of the class.

To assign attributes to the instance of the class, use the keyword 'self' and the 'dot' operator 
from inside of the constructor, see below class example.

```
class Person:

     def __init__(self, name, age): # class constructor
         #note that the attributes are not declared outside of the constructure.
         self.name = name # class variable
         self.age = age # class variable

     def greet(self): # class function to print a greeting
         print("Hello, my name is %s!" % self.name)
```

The constructor is a method and can perform type checking of parameters, basically anything a 
method can do, **except:** return a value.

use 'def __str__(self):' method to return string representation to the end user
use 'def __repr__(self):' method to return output to the dev

**Inheritance**, is where one class the child inherits the attribute and methods of the parent.
eg. 
```
Class Parent():
    ....
Class Child(Parent): <-You can see the Parent being inherited by the child, this is how you know
                        if a class is a child or not.
    ....
```

You can call the parents constructor from inside the child constructor and modify it
You can overwrite a parents method by rewriting that method
A child class inherits all the attributes and methods of the parent and you only need to create a __str__()
to test this.

Multi-Level inheritance is where one class inherits from another then another class inherits from that class
eg. class GrandParent(): > class Parent(GrandParent): > class Child(Parent):

Multiple inheritance is where a class can inherit from more than one Parent Class.
eg. class ChildClass (Parent1, Parent2, Parent3, ...):

The built-in super function allows the child class (or subclass) to access inherited methods of the 
parent class (or superclass) that have been overwritten in the child class. When we called the 
parent class’s methods super().__init__(name) and super().greet(), we didn’t explicitly add self as a parameter 
to these methods.


####Iteration and Loops
For loops, syntax is:
```
for index in sequence:
    statement
```
for loops must include the keyword 'in', for loops expects a sequence and that
is why range is useful.  Example if you want to use the for loop to iterate over
a list and return the index, you need to use range(len(list)). len() will return 
a integer and range() will return a list = [0, ...,number-of-items-in-list]

#####Important For loop information:
In python the iterator/indexer does not need to be define ahead of time unlike in java.
In the example below the iterator/indexer 'i' is automatically inferred from range() function
and you must use the range function to increase/decrease the indexer, in our example we 
increase the iterator by 2 everytime we loop through.  Using i += 1 at the end of the for loop
does not affect the indexer 'i'!
```
def sumList(l):
    sum = 0
    for i in range(0,len(l),2):
        sum = sum + l[i]
    return sum

print(sumList(l))
```

Increment:
x += 1, will increment by 1

Decrement:
x -=1, will decrement by 1

The enumerate function is very useful since it returns an iterable that give you the index and value 
of items in a list for example. link: https://www.geeksforgeeks.org/enumerate-in-python/
You can also choose what index to start iterating from too.

While loops syntax is:
```
while(condition):
    statement
```

To find out if an element is in a list you can use the 'in' operator: 'r' in 'bars'
To find the location of an element in a list you can use the index method: [1, 2, 4].index[2]

To manipulate lists and AVOID list out of bound error which is usually caused by using x + 1 where x
is a list index USE the range() function.  Range(len(l)) returns a sequence of number starting at ZERO
and ending one less than the number specified in the range. example range(2) = [0,2]

```
def has_duplicates(list):
  flag = 0
  for i in range (len(list)):
    for j in range (i+1,len(list)): <- Avoid list out of bounds error
        if (list[i] == list[j]):
          flag = 1
  if (flag == 1): 
     return True
  else:
     return False
```

####Modules
Modules are python files containing functions and variables of all types such
as dictionaries, arrays, objects etc.  Use the "import" statement to use a module.

####Functions
Functions with in a module only execute when called.  If your module has print statements
outside of functions those prints statements will execute.

Functions with out return statements, when called will execute whatever
code is in the body of the function and also print 'none' to the terminal

Two kinds of functions: 
1. parameterized functions are functions that takes in parameters
2. Non-parameterized functions are functions that do not accept parameters

Return statements evaluate any expression you pass to it. eg return x<5<y will
return true if you pass f(3,6) to the function

#####Recursion
Recursion is the most important concept when using a function.  Recursion is when a functions 
calls itself again and again until it reaches its base condition.  
There are two parts of recursion:
1. Base condition
2. Recursive function

eg:The sum of all numbers from 1 up to and including that input natural number n:
```
def sum_N_Numbers (n):
  if n <= 1:
    return n //base  condition
  else:
    return n + sum_N_Numbers (n-1) //recursive function
```

####Strings
"for char in string" can iterate over characters of a string

String.find('substring/char',start index, end index) use this method to find substring
or characters with in a string

ONLY Strings can be concatenated using '+' . If you want to join together integers and strings
then using ',' before and after the non-string value and python will automatically apply a space.
examples:
print("index: " + str(index) + " value: " + str(value))
print("index:", index, "value:", value)

####Dictionaries
Dictionaries hold key-value pairs, they are indexed by keys and not numbers like lists. 
Dictionaries are created using curly braces {} and accessed using square brackets [].
Create a dictionary in two ways:
1. new_dict = dict()
2. new_dict = {}

Dictionaries are indexed by keys, which can be any immutable type; strings and numbers can 
always be keys. Tuples can be used as keys if they contain only strings, numbers, or tuples; 
if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. 
You can’t use lists as keys, since lists can be modified in place using index assignments, slice 
assignments, or methods like append() and extend().

A dictionary order is not maintained, so every thing you print a dictionary the order of
keys change.**To create an ordered dictionary:** 
```
from collections import OrderedDict

#create an ordered dictionary called ages
ages = OrderedDict()
```

Ordered dictionary preserves the order in which keys are inserted.

Use the **items()** method to return a dictionary's keys their values in a for loop. for k,v in dict1.items():
The items() method returns 2 iterators/indices and they are a key iterator and a value iterator

A for loop (for x in dict:) returns a key iterator, so you have to access value by using the key as an index.
eg print(dict1[x])

The iterate over just the values of a dictionary use the **values()** method. 
eg for value in dict.values(): print (value)

to iterate over a nested dictionary, just remember that the value of the parent dictionary is second dictionary 
that you must extract the key,value pair from



####Lists
List comprehension = (expression reference predicate)
eg: (x**2 for x in range(start,n-1,incrementer) if (x%2 == 0) and (x%3==0))

lists can be concatenated using the '+' symbol

list.append(90) will insert the value into list however if you do list.append(list) you will
have list[1,2,3, list[1,2,3]] a list with in a list

Lists are created using square bracket.  we access elements in them by providing the list name
followed by square brackets that enclose the index number of the value you want.
eg: list_name[1] 

####Numbers
Range() function: range(start, End, increment)
range(10) = 0 to 9
range(0, 10, 2) = 0,2,4,6,8

% modulus give you the remainder eg 3%2  = 1

// gives you the quotient or whole number left of the decimal. eg 3/2 = 1

'parity' refers to odd or even





