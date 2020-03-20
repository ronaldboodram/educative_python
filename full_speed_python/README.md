#Full Speed Python

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

String can be concatenated using '+'

####Lists
List comprehension = (expression reference predicate)
eg: (x**2 for x in range(start,n-1,incrementer) if (x%2 == 0) and (x%3==0))

lists can be concatenated using the '+' symbol

list.append(90) will insert the value into list however if you do list.append(list) you wil
have list[1,2,3, list[1,2,3]] a list with in a list

####Numbers
range(10) = 0 to 9
range(0, n-1, 2) = 0,2,4,6,8

% modulus give you the remainder eg 3%2  = 1

// gives you the quotient or whole number left of the decimal. eg 3/2 = 1

'parity' refers to odd or even




