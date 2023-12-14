# Python Sets
Sets are unordered collection of data items. They store multiple items in a single variable. \
Set items are separated by commas and enclosed within curly brackets { }. \
Sets are unchangeable, meaning you cannot change items of the set once created. Sets do not contain duplicate items.\
Set is a collection of well-defined objects.

*Example 01* :
```python
s = {2, 4, 5, 6}  #set eliminate repeated value
print(s)
```

Output:
```
{2, 4, 6}
```
=========================================================
*Example 02*:
```python
info = {"Carla", 19, False, 5.9, 19}
print(info) #it prints unordered data
```

Output:
```
{19, False, Carla, 5.9}
```
Here we see that the items of set occur in random order and hence they cannot be accessed using index numbers. Also sets do not allow duplicate values.

---
**Quick Quiz:** Try to create an empty set. Check using the type() function whether the type of your variable is a set.

```python
# harry = {}
# print(type(harry))  #it prints dictionary - wrong method

harry = set()   # to create empty set
print(type(harry)) 
```

## Accessing set items:
 
### Using a For loop
You can access items of set using a for loop.

*Example* :
```python
info = {"Carla", 19, False, 5.9, 19}
for value in info:
    print(value)
```

Output:
```
19
False
Carla
5.9
```