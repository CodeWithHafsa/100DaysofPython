# List Methods:
1. append()
2. sort()
3. reverse()
4. index()
5. count()
6. copy()
7. insert()
8. extend()

## 1. append():
This method appends items to the end of the existing list.
*Example*
```python
l = [11, 45, 1, 2, 4, 6]
print(l)
l.append(7) #append
print(l)
```

Output:
```
[11, 45, 1, 2, 4, 6]
[11, 45, 1, 2, 4, 6, 7]
```

## 2. sort():
This method sorts the list in ascending order. The original list is updated.

*Example* :
```python
l = [11, 45, 1, 2, 4, 6]
print(l)
l.sort() #sort in ascending order
print(l)
```

Output:
```
[1, 2, 4, 6]
[1, 2, 4, 6]
```

* For descending order give ---> reverse=True

*Example* :
```python
l = [11, 45, 1, 2, 4, 6]
print(l)
l.sort(reverse=True) #sort in descending order
print(l)
```

Output:
```
[1, 2, 4, 6]
[6, 4, 2, 1]
```

## 3. reverse():
This method reverses the order of the list. 

*Example*
```python
l = [11, 45, 1, 2, 4, 6]
print(l)
l.reverse() #reverse original list
print(l)
```

Output:
```
[1, 2, 4, 6]
[6, 4, 2, 1]
```

## 4. index():
This method returns the index of the first occurrence of the list item.

*Example*
```python
l = [11, 45, 1, 2, 4, 6]
print(l)
print(l.index(1)) # returns first occurrence
```

Output:
```
[1, 2, 4, 6]
0
```

## 5. count():
Returns the count of the number of items with the given value.

*Example*
```python
l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l.count(1)) #count how many times '1' came in list
print(l)
```

Output:
```
3
[11, 45, 1, 2, 4, 6, 1, 1]
```

## 6. copy():
Returns copy of the list. This can be done to perform operations on the list without modifying the original list.

* *Example: if we don't use copy*
*Example*
```python
l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
m = l
m[0] = 0 
print(l) #it makes changes in both m and l lists.
print(m)
```

Output:
```
[11, 45, 1, 2, 4, 6, 1, 1]
[0, 45, 1, 2, 4, 6, 1, 1]
[0, 45, 1, 2, 4, 6, 1, 1]
```

* *Example: if we use copy*
```python
l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
m = l.copy()
m[0] = 0 
print(l) 
print(m) #it only changes m list.
```

Output:
```
[11, 45, 1, 2, 4, 6, 1, 1]
[11, 45, 1, 2, 4, 6, 1, 1]
[0, 45, 1, 2, 4, 6, 1, 1]
```

## 7. insert():
This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.

*Example*
```python
l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
l.insert(1, 899) #at index[1] value changes to 899.
print(l)
```

Output:
```
[11, 45, 1, 2, 4, 6, 1, 1]
[11, 899, 45, 1, 2, 4, 6, 1, 1]
```

## 8. extend():
This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.

*Example*
```python
l = [11, 45, 1, 2, 4, 6, 1, 1]
m =[900, 1000, 1100]
l.extend(m) #open m and add at the end of l
print(l)
```

Output:
```
[11, 45, 1, 2, 4, 6, 1, 1, 900, 1000, 1100]
```

## Concatenating two lists:
You can simply concatenate two lists to join two lists. (It is similar to extend)

*Example*
```python
l = [11, 45, 1, 2, 4, 6, 1, 1]
m =[900, 1000, 1100]
k = l + m
print(k)
```

Output:
```
[11, 45, 1, 2, 4, 6, 1, 1, 900, 1000, 1100]
```

### [Next Lesson>>](https://replit.com/@CodeWithHafsa/Python-24-Tuples-in-Python?v=1)