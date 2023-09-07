## 4. Variable-length arguments:
Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.

There are two ways to achieve this:
1. Arbitrary Arguments
2. Keyword Arbitrary Arguments

#### Arbitrary Arguments:
While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple.

*Example 01* :
```python
def average(*numbers): 
    #print(type(number)) # tuple - it takes input as tuple/list.
    sum = 0 #initialize
    for i in numbers:
        sum = sum + i
        print("Average is: ", sum/len(numbers))

#average(5,6)  #output: Average is:  5.5
average(5, 6, 7, 1) #output: Average is:  4.5

#with the help of above function, we can take average of as many numbers as we want
```

Output:
```
Average is:  4.5
```
========================================================
*Example 02* :
```python
def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("James", "Buchanan", "Barnes")
```
Output:
```
Hello, James Buchanan Barnes
```
---
#### Keyword Arbitrary Arguments:
While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of dictionary.

*Example 01* :
```python
def name(**name):
    #print(type(number)) # dictionary - it takes input as dictionary.
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")
```
Output:
```
Hello, James Buchanan Barnes
```

## return Statement
The return statement is used to return the value of the expression back to the calling function.

*Example 01* :
```python
def average(*numbers): 
    sum = 0 #initialize
    for i in numbers:
        sum = sum + i
        return sum/len(numbers)

c = average(5, 6, 7, 1)
print(c)   #return function stores value and save it in varaible
```

Output:
```
4.75
```
========================================================
*Example 02* :
```python
def average(*numbers): 
    sum = 0 #initialize
    for i in numbers:
        sum = sum + i
        return 7    #If we use use more thane one return statement, then jo bhi pehley return mileyga, yeh return statement ussy return kareygi.
        return sum/len(numbers)

c = average(5, 6, 7, 1)
print(c)   #return function stores value and save it in varaible
```

Output:
```
7 
```
========================================================
*Example 03* :
```python
def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))
 ```

Output:
```
Hello, James Buchanan Barnes
```