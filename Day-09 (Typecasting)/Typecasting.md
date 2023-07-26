# Typecasting in Python
The conversion of one data type into the other data type is known as 'type casting' in python or 'type conversion' in python.

Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc. for the type casting in python.

**Example**
```python
a = "1"  #string
b = "2"  #string
print(a + b)

c = 1 #integar
d = 2 #integar
print(a + b)
```

Output:
```markup
12
3
```

## Types of Typecasting
1. Explicit Conversion (Explicit type casting in python)
2. Implicit Conversion (Implicit type casting in python).

### 1. Explicit typecasting:
The conversion of one data type into another data type, done via developer or programmer's intervention or manually as per the requirement, is known as 'explicit type conversion'. 

It can be achieved with the help of Python’s built-in type conversion functions such as int(), float(), hex(), oct(), str(), etc .

### Example of explicit typecasting:
```python
a = "1" #string 
b = "2"  #string
print(int(a) + int(b)) #int - convert string into integar and then perform operation.
```

Output:
```markup
3 
```

* If we write "1hafsa" in above example, so it can't be converted into integar. So, python will create error in it. It means to perform "typecasting" code should be valid. 
___

### 2. Implicit type casting:
Data types in Python do not have the same level i.e. ordering of data types is not the same in Python. Some of the data types have higher-order, and some have lower order. 

Python converts a smaller data type to a higher data type to prevent data loss. This is called, 'implicit typecasting' in python.

### Example of implicit type casting:
```python
a = 8 #a is int
b = 1.9 #b is float
print(a + b)
```

### Ouput:
```markup
9.9 
```

* python coverts int into float than add float + float - and gives answer in float. 

### [Next Lesson>>](https://replit.com/@CodeWithHafsa/Pyhton-10?v=1)