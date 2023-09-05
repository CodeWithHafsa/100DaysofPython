# Introduction to Loops:
Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loops. Based on this loops are further classified into following main types; 
- for loop
- while loop 

# for Loop:
for loops - can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.

### *Example: iterating over a string*
*Example 1*:
```python 
name = 'Abhishek'
for i in name:
    print(i, end=", ")
```

Output:
```
A, b, h, i, s, h, e, k, 
```
========================================================

*Example 2*:
```python 
name = 'Abhishek'
for i in name:
    print(i)
    if(i == "b"):
        print("This is something special!")
```

Output:
```
A
b
This is something special!
h
i
s
h
e
k
```

### Example: iterating over a list:
*Example 1*:
``` python 
colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
    print(color)
```

Output:
```
Red
Green
Blue
Yellow
```
========================================================

*Example 2*:
``` python 
colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
    print(color)
    for i in color: #to iterate a list
        print(i)
```

Output:
```
Red
R
e
d
Green
G
r
e
e
n
Blue
B
l
u
e
Yellow
Y
e
l
l
o
w
```

Similarly, we can use loops for lists, sets and dictionaries.

## range():
What if we do not want to iterate over a sequence? What if we want to use for loop for a specific number of times?

Here, we can use the range() function.

* The loop starts from 0 by default and increments at each iteration. 
* But we can also loop over a specific range.

*Example 1*:
* To print from 0 to 4:
```python
for k in range(5): #from 0 to 4
    print(k)
```

Output:
```
0
1
2
3
4
```
========================================================
*Example 2*:
* To print from 1 to 5:
```python
for k in range(5): #from 1 to 5
    print(k + 1)
```

Output:
```
1
2
3
4
5
```
========================================================
*Example 3*:
* To print from 2 to 6:
```python
for k in range(5): #from 2 to 6
    print(k + 2)
```

Output:
```
2
3
4
5
6
```
========================================================
*Example 4*:
* To print from 1 to 8:
```python
for k in range(1, 9): # from 1 to 8
    print(k)
```

Output:
```
1
2
3
4
5
6
7
8
```
========================================================
* To print from 1 to 20001:
```
for k in range(1,2000): #from 1 to 2000 (too long)
    print(k)
```

## range() using third parameter 'step':
Explore about third parameter of range (ie range(x, y, z))

*Example* :
```python
# 3 parameter range: start,end,step
for k in range(1, 12, 3):
  print(k)
```

How it works:
```
Here: start =1, end =12 and step = 3

# it prints 1,4,7,10 b/c list starts with 1 
# Then, 1+3 = 4 
# Then 1+3+3 = 7
# Then 1+3+3+3 =10
# Then 1+3+3+3+3 = 13 - but it doesn't print 13 b/c a/c to range string ends at 12.
```

Output:
```
1
4
7
10
```
