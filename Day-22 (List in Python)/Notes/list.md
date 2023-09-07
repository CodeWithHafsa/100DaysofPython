# List in Python
- Lists are ordered collection of data items.
- They store multiple items in a single variable.
- List items are separated by commas and enclosed within square brackets [].
- Lists are changeable meaning we can alter them after creation.

*Example 1*
```python
marks = [3, 5, 6, "Harry", True]
print(marks)
print(type(marks))
print(marks[0])  #indexing
print(marks[1])  #indexing
print(marks[2])  #indexing
print(marks[3])  #indexing
print(marks[4])  #indexing
#print(marks[5])  #indexing(here 5th index is not prsenet)
```

Output:
```
[3, 5, 6, 'Harry', True]
<class 'list'>
3
5
6
Harry
True
```
---
*Example 2*
```python
lst1 = [1,2,2,3,5,4,6]
lst2 = ["Red", "Green", "Blue"]
print(lst1)
print(lst2)
```

Output:
```
[1, 2, 2, 3, 5, 4, 6]
['Red', 'Green', 'Blue']
```
---
*Example 3*
```python
details = ["Abhijeet", 18, "FYBScIT", 9.8]
print(details)
```

Output:
```
['Abhijeet', 18, 'FYBScIT', 9.8]
```
As we can see, a single list can contain items of different data types.

# List Index:
Each item/element in a list has its own unique index. This index can be used to access any particular item from the list. The first item has index [0], second item has index [1], third item has index [2] and so on.

*Example* :
```python
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
```

# Accessing list items
We can access list items by using its index with the square bracket syntax []. 
 
For example colors[0] will give "Red", colors[1] will give "Green" and so on...

## 1. Positive Indexing:
As we have seen that list items have index, as such we can access items using these indexes.

*Example* :
```python
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
print(colors[2])
print(colors[4])
print(colors[0])
```

Output:
```
Blue
Green
Red
```

## 2. Negative Indexing:
Similar to positive indexing, negative indexing is also used to access items, but from the end of the list. The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.

*Example 1*:
```python
marks = [3, 5, 6, "Harry", True]
print(marks[-3]) # Negative index
print(marks[len(marks)-3 ]) # Positive index
print(marks[5-3]) # Positive index
print(marks[2]) # Positive index
```

Output:
```
6
6
6
6
```
---
*Example 2* :
```python
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [-5]    [-4]    [-3]     [-2]      [-1]
print(colors[-1])
print(colors[-3])
print(colors[-5])
```
Output:
```
Green
Blue
Red
```

## Check whether an item in present in the list?
We can check if a given item is present in the list. This is done using the `in` keyword.

* *Example 1* :
```python
marks = [3, 5, 6, "Harry", True]
if 7 in marks:
    print("Yes")
else:
    print("No")
```

Output:
```
No
```
---
* *Example 2* :
```python
marks = [3, 5, 6, "Harry", True]
if "Harry" in marks:
    print("Yes")
else:
    print("No")
```

Output:
```
Yes
```
---
* *Example 3* :
```python
if "6" in marks:
    print("Yes")
else:
    print("No")
```

Output:
```
No
```
---
* *Example 4* :
```python
if "Ha" in "Harry": #same thing apply for string as well
    print("Yes")
else:
    print("No")
```

Output:
```
Yes
```
---
* *Example 5* :
```python
if "ary" in "Harry":
    print("Yes")
else:
    print("No")
```

Output:
```
No
```
---
* *Example 6* :
```python
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Yellow" in colors:
    print("Yellow is present.")
else:
    print("Yellow is absent.")
```

Output:
```
Yellow is present.
```

## Key Point:
* Tuples cannot change / alter.
* List can be change / alter.
