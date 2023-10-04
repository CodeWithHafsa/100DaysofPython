# Python Tuples
Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed within round brackets (). Tuples are unchangeable meaning we can not alter them after creation.

```python
tup = (1, 5, 6)
print(type(tup), tup)
```

Output:
```
<class 'tuple'> (1, 5, 6)
```
---
* If we made a one element tuple, so `comma` is neccessary, if we don't use comma then python consider it as an `integar`.
```python
# without comma 
tup = (1)  #output: <class 'int'> (1)

# with comma
tup = (1,)  #output: <class 'tuple'> (1,)
print(type(tup), tup)
```

Output:
```
<class 'tuple'> (1,)
```
---
* Tuples are unchangable, while lists are changable.
```python
list = (1, 2, 76, 342, 32) #list
list[0] = 90 
print(type(tup), list)
#output: <class 'list'> (90, 2, 76, 342, 32)

tup = [1, 2, 76, 342, 32]  #tuple
# tup[0] = 90
print(type(tup), tup)   
#output: Error - because tuples are unchangable
```
---
* We can also add any `string` and `boolean` datatype in a tuple.
```python
tup = [1, 2, 76, 342, 32, "green", True]  #tuple
print(type(tup), tup)
```

Output:
```
<class 'tuple'> [1, 2, 76, 342, 32, "green", True]
```

## Examples:
*Example 01* :
```python
tuple1 = (1,2,2,3,5,4,6)
tuple2 = ("Red", "Green", "Blue")
print(tuple1)
print(tuple2)
```

Output:
```
(1, 2, 2, 3, 5, 4, 6)
('Red', 'Green', 'Blue')
```
========================================================
*Example 02* :
```python
details = ("Abhijeet", 18, "FYBScIT", 9.8)
print(details)
```

Output:
```
('Abhijeet', 18, 'FYBScIT', 9.8)
```

## Some information:
* List - written in sqaure brackets [] and are changable (mutable).
* Tuple - written in round brackets () and are unchangable (immutable).

### [Next Leeson>>](https://replit.com/@CodeWithHafsa/Python-25?v=1)