# Python Functions
A function is a block of code that performs a specific task whenever it is called. 

In bigger programs, where we have large amounts of code, it is advisable to create or use existing functions that make the program flow organized and neat.

There are two types of functions:

1. Built-in functions - Didn't need to define using 'def' function
2. User-defined functions - Need to define using 'def' function

## Built-in functions:
These functions are defined and pre-coded in python.\
Some examples of built-in functions are as follows:

min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.

## User-defined functions:
We can create functions to perform specific tasks as per our needs.\
Such functions are called user-defined functions.

### Syntax:
```python
def function_name(parameters):
  pass
  # Code and Statements
```

 - Create a function using the def keyword, followed by a function name, followed by a paranthesis (()) and a colon(:).
 - Any parameters and arguments should be placed within the parentheses.
 - Rules to naming function are similar to that of naming variables.
 - Any statements and other code within the function should be indented.

---
### Calling a function:
We call a function by giving the function name, followed by parameters (if any) in the parenthesis.

*Example* :
```python
def name(fname, lname):
    print("Hello,", fname, lname)

name("Sam", "Wilson")
```

Output:
```
Hello, Sam Wilson
```


## Examples:
*Geometric Mean without using function*
```python
a = 9
b = 8
gmean1 = (a*b) / (a+b)  #geometric mean
print(gmean1)

c = 8
d = 7
gmean1 = (c*d) / (c+d)  #geometric mean
print(gmean1)
```

Output:
```
4.235294117647059   #geometric mean of a and b
3.7333333333333334  #geometric mean of c and d
```
---

*Geometric Mean and Greater tahnwith function*
```python
def calculateGmean(a, b): #function for geometric mean
  mean = (a*b) / (a+b)
  print(mean)

def isGreater(a,b): #function for greater than
    if (a>b): #function definition(body)
        print("First number is greater")
    else:
        print("Second number is greater or equal")

def islesser(a,b):
    pass #means - pass this function (I will write it after)

a = 9
b = 8
calculateGmean(a, b)
isGreater(a,b)
# gmean1 = (a*b) / (a+b)  #geometric mean without function
# print(gmean1)

c = 8
d = 7
calculateGmean(c, d) #short form for geometric mean
isGreater(c,d)  #shortform for greater than
# gmean1 = (c*d) / (c+d)   #geometric mean without function
# print(gmean1)
```

Output:
```
First number is greater
4.235294117647059      
First number is greater
3.7333333333333334 
```