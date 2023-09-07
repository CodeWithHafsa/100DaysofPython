# Range of Index:
You can print a range of list items by specifying where you want to start, where do you want to end and if you want to skip elements in between the range. 

Syntax:
```python
listName[start : end : jumpIndex]
```
* Note: jump Index is optional. It is also known as step. 
* Range of index = slicing

*Example*:
```python
marks = [3, 5, 6, "Harry", True, 6, 7, 2, 32, 345, 23]
print(marks)
print(marks[1:-1]) #len=11, 11-1=10 #print(marks[1:10])
print(marks[1:8])
print(marks[1:8:3])
```

Output:
```
[3, 5, 6, 'Harry', True, 6, 7, 2, 32, 345, 23]
[5, 6, 'Harry', True, 6, 7, 2, 32, 345]
[5, 6, 'Harry', True, 6, 7, 2]
[5, True, 2]
```
* Note: The element of the end index provided will not be included. 

## Key Points :
* Note: The element of the end index provided will not be included.
```
animals = ["cat", "dog", "bat", "mouse", "dolphin", "horse", "donkey", "goat", "cow"]
```
---
* Here, we provide index of the element from where we want to start and the index of the element till which we want to print the values.
```python
print(animals[3:7])	#using positive indexes
print(animals[-7:-2])	#using negative indexes'
```
---
* When no end index is provided, the interpreter prints all the values till the end.
```python
print(animals[4:])	#using positive indexes
print(animals[-4:])	#using negative indexes
```
---
* When no start index is provided, the interpreter prints all the values from start up to the end index provided.
```python
print(animals[:6])	#using positive indexes
print(animals[:-3])	#using negative indexes
```
---
* Here, we have not provided start and index, which means all the values will be considered. But as we have provided a jump index of 2 only alternate values will be printed. 
```python
print(animals[::2])		#using positive indexes
print(animals[-8:-1:2])	#using negative indexes
```
---
* Here, jump index is 3. Hence it prints every 3rd element within given index.
```python
print(animals[1:8:3])
```

