# Tuple methods
As tuple is immutable type of collection of elements it have limited built in methods.

## 1. count() Method
The count() method of Tuple returns the number of times the given element appears in the tuple.

### Syntax:
```python
tuple.count(element)
```

*Example* :
```python
tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)
```

Output
```
3
```

## 2. index() method
The index() method returns the first occurrence of the given element from the tuple.

### Syntax:
```python
tuple.index(element, start, end)
```

Note: This method raises a ValueError if the element is not found in the tuple.

*Example 01* :
```python
tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = tuple1.index(3)  #tells index of first occurence
print('First occurrence of 3 is', res)
```

Output
```
3
```
---
*Example 02* :
```python
tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2, 3)
res = tuple1.index(3, 4, 8)  #here 4:8 slice the tuple, after slicing the first occurence of 3 returns by index
print('First occurrence of 3 is', res)
```

Output
```
5
```

## 3. len() method
The len() method tells the length of the tuple.

### Syntax:
```python
len(element)
```

*Example* :
```python
tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2, 3)
res = len(tuple1)  
print('length of tuple', res)
```

Output:
```
length of tuple 10
```

### [Next Lesson>>](https://replit.com/@CodeWithHafsa/KBC-27-and-39?v=1)