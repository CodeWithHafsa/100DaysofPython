# Tuple Indexes
Each item/element in a tuple has its own unique index. This index can be used to access any particular item from the tuple. The first item has index [0], second item has index [1], third item has index [2] and so on.

### How it works:
```python
country = ("Spain", "Italy", "India",)
#            [0]      [1]      [2]              
```

## Accessing tuple items:
 
### I. Positive Indexing:
As we have seen that tuple items have index, as such we can access items using these indexes.

### II. Negative Indexing:
Similar to positive indexing, negative indexing is also used to access items, but from the end of the tuple. The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.

*Example 01* :
```python
country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]       [3]        [4]  

# Positive indexing
print("Positive indexing")
print(country[0])
print(country[1])
print(country[2])

# Negative indexing
print("\nNegative indexing")
print(country[-1]) # Similar to print(country[len(country) - 1])
print(country[-3])
print(country[-4])
```

Output:
```
Positive indexing
Spain
Italy
India

Negative indexing
Germany
India
Italy
```
========================================================
*Example 02* :
```python
tup = (1,  2,  76,  342, 32, "green", True)
#     [0] [1]  [2]  [3]  [4]   [5]    [6]

print(len(tup)) #output: 7
print(tup[0])  #positive indexing
print(tup[-1]) #negative indexing= len(tup) -1 => 7-1 =6
print(tup[2])
print(tup[3])
```

Output:
```
7
1
True
76
342
```

## III. Check for item:
We can check if a given item is present in the tuple. This is done using the `in` keyword.\
*Example 01* :
```python
tup = (1,  2,  76,  342, 32, "green", True)
if 342 in tup:
    print("Yes 342 is present in tuple")

# if 3421 in tup: (3421 is not present in the tuple, so it wil not print anything)
#     print("Yes 342 is present in tuple")
```

Output:
```
Yes 342 is present in tuple
```

========================================================
*Example 02* :
```python
country = ("Spain", "Italy", "India", "England", "Germany")
if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")
  ```

Output:
```
Germany is present.
```

========================================================
*Example 03* :
```python
country = ("Spain", "Italy", "India", "England", "Germany")
if "Russia" in country:
    print("Russia is present.")
else:
    print("Russia is absent.")
  ```

Output:
```
Russia is absent.
```