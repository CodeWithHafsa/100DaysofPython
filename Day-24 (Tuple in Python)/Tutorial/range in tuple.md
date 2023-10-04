### IV. Range of Index:
It is same as slicing and returns a new tuple because tuple is unchangeable.

You can print a range of tuple items by specifying where do you want to start, where do you want to end and if you want to skip elements in between the range.

### Syntax:
```python
Tuple[start : end : jumpIndex]
```
Note: jump Index is optional. \
The element of the start index provided will included.\
The element of the end index provided will not be included.

*Example* :
```python
tup = (1, 2, 76, 342, 32, "green", True)
tup2 = tup[1:4] #slicing
print(tup2) # returns a new tuple
```

Output:
```
(2, 76, 342)
```

## Some Practice Examples:
### Example: Printing elements within a particular range:
```python
animals = ("cat", "dog", "bat", "mouse", "horse", "donkey", "goat", "cow")
#            0      1      2       3       4         5         6       7

print(animals[3:7])     #using positive indexes 
print(animals[-7:-2])   #using negative indexes
```

Output:
```
('mouse', 'horse', 'donkey', 'goat')
('dog', 'bat', 'mouse', 'horse', 'donkey')
```

Here, we provide index of the element from where we want to start and the index of the element till which we want to print the values. 
Note: The element of the end index provided will not be included.

---
### Example: Printing all element from a given index till the end
```python
animals = ("cat", "dog", "bat", "mouse", "lion","horse", "donkey", "goat", "cow")
#            0      1      2       3        4         5        6      7      8

print(animals[4:])      #using positive indexes
print(animals[-4:])     #using negative indexes
```
### Output:
```
('lion', 'horse', 'donkey', 'goat', 'cow')
('horse', 'donkey', 'goat', 'cow')
```
When no end index is provided, the interpreter prints all the values till the end.

----
### Example: printing all elements from start to a given index
```python
animals = ("cat", "dog", "bat", "mouse", "lion", "horse", "donkey", "goat", "cow")
#            0       1     2       3        4       5         6       7       8

print(animals[:6])      #using positive indexes
print(animals[:-3])     #using negative indexes
```

Output:
```
('cat', 'dog', 'bat', 'mouse', 'lion', 'horse')
('cat', 'dog', 'bat', 'mouse', 'lion', 'horse')
```
When no start index is provided, the interpreter prints all the values from start up to the end index provided. 

---
### Example: Print alternate values
```python
animals = ("cat", "dog", "bat", "mouse", "lion", "horse", "donkey", "goat", "cow")
#            0       1     2       3        4       5         6       7       8

print(animals[::2])     #using positive indexes
print(animals[-8:-1:2]) #using negative indexes
```
Output:
```
('cat', 'bat', 'lion', 'donkey', 'cow')
('dog', 'mouse', 'horse', 'goat')
```
Here, we have not provided start and end index, which means all the values will be considered. But as we have provided a jump index of 2 only alternate values will be printed. 

---
### Example: printing every 3rd consecutive withing given range
```python
animals = ("cat", "dog", "bat", "mouse", "lion", "horse", "donkey", "goat", "cow")
#            0       1     2       3        4       5         6       7       8

print(animals[1:8:3])
```

Output:
```
('dog', 'lion', 'goat')
```
Here, jump index is 3. Hence it prints every 3rd element within given index.