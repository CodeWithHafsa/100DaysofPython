# List Comprehension:
List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.

### Syntax:

List = [Expression(item) for item in iterable if Condition]

* **Expression**: It is the item which is being iterated.
* **Iterable**: It can be list, tuples, dictionaries, sets, and even in arrays and strings.
* **Condition**: Condition checks if the item should be added to the new list or not. 
---

* *Example 1* :
```python
lst = [i for i in range(4)]
print(lst)
```

Output:
```
[0, 1, 2, 3]
```
---

* *Example 2* :
```python
lst = [i*i for i in range(4)]
print(lst)
```

Output:
```
[0, 1, 4, 9]
```
---

* *Example 3* :
```python
lst = [i*i for i in range(10) if i%2==0] #if i is divisible by 2 then show number
print(lst)
```

Output:
```
[0, 4, 16, 36, 64]
```
---

* *Example 4 : Accepts items with the small letter “o” in the new list* 
```python
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)
```

Output:
```
['Milo', 'Bruno', 'Rosa']
```
---

* *Example 5: Accepts items which have more than 4 letters*

```python
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)
```

Output:
```
['Sarah', 'Bruno', 'Anastasia']
```