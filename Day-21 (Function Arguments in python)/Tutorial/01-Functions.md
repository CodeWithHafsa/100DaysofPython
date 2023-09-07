# Function Arguments and return statement:
There are four types of arguments that we can provide in a function:

- Default Arguments
- Keyword Arguments
- Variable length Arguments
- Required Arguments

## 1. Default arguments:
We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument.

*Example 1* :
```python
def average(a=9, b=1): #default arguments
    print("The average is ", (a+b)/2)
average()
```
Output:
```
The average is  5.0
```
=========================================================

*Example 2* :
```python
def average(a=9, b=1): #default arguments
    print("The average is ", (a+b)/2)
average(1,5) #it ignores above values and take a=1 and b=5
```
Output:
```
The average is  3.0
```
=========================================================

*Example 3* :
```python
def average(a=9, b=1): #default arguments
    print("The average is ", (a+b)/2)
average(5) #here only value of a is given so a=5 and b=1 (i.e. deafult value given above)
```

Output:
```
The average is  3.0
```

=========================================================

*Example 4* :
```python
def average(a=9, b=1): #default arguments
    print("The average is ", (a+b)/2)
average(b=9) #here only value of b is given so b=9 and a=9 (i.e. deafult value given above)
```

Output:
```
The average is  9.0
```

=========================================================

*Example 5* :
```python
def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Amy")
```

Output:
```
Hello, Amy Jhon Whatson
```

## 2. Keyword arguments:
We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.

*Example 1* :
```python
def average(a=9, b=1): #keyword arguments
    print("The average is ", (a+b)/2)
average(b=9, a=21) #here order of value doesnot matters
```

Output:
```
The average is  15.0
```

=========================================================

*Example 2* :
```python
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")
```

Output:
```
Hello, Jade Peter Wesker
```

## 3. Required arguments:
In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.

*Example 1*:
```python
def average(a, b, c=1): #required arguments
    print("The average is ", (a + b + c) / 2)
average(5,6) 

#In above function value of a and b is not given, so we have given there values here a=5, b=6 and c=1 (default value given above)
```

Output:
```
The average is  6.0
```

=========================================================

*Example 2*:
```python
def average(a, b): #required arguments
    print("The average is ", (a+b)/2)
average(4, 6)
```

Output:
```
The average is  5.0
```

=========================================================

*Example 3*:
```python
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name("Peter", "Ego", "Quill")
```

Output:
```
Hello, Peter Ego Quill
```
