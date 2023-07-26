# Variables and Data Types
### Variable
Variable - is like a container that holds data
```python
a = 1234453734563455
print(a)
b = "Harry"
print(b)
```

Output:
```markup
1234453734563455
Harry
```
---

### Data Type
Data type - specify type of value which a variable can store. It is required in programming to perform 'operations'.
* To perform operations - data type should be same. 
```python
a = 123
a1 = 9
print(a + a1)
```

Output:
```markup
132
```

* There are four different data types.
```python
a = 1 #integar
b = True #boolean
c = "Harry" #string
d = None #null data type
print("The type of a is ", type(a))
print("The type of a is ", type(b))
print("The type of a is ", type(c))
```

Output:
```markup
The type of a is <class 'int'>
The type of b is <class 'bool'>
The type of c is <class 'str'>
```
___

## Built-in Data Types:
## 1. Numeric data: int, float, complex
* int: 3, -8, 0
* float: 7.349, -9.0, 0.0000001
* complex: 6 + 2i 

**Example:**

```python
a = 3
b = 7.38
c = complex(8,2)
print(a)
print(b)
print(c)
print("The type of a is ", type(a))
print("The type of a is ", type(b))
print("The type of a is ", type(c))
```

Output:
```markup
3
7.38
8+2j
The type of a is <class 'int'>
The type of a is <class 'float'>
The type of a is <class 'complex'>
```

## 2. Text data: str   
str: "Hello World!!!", "Python Programming"

## 3. Boolean data:
Boolean data consists of values True or False. #tells Yes and No.

## 4. Sequenced data: list, tuple
* list and tuple

**list:** A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. Lists are mutable and can be modified after creation.

**Example:**

```python
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)
```

Output:
```markup
[8, 2.3, [-4, 5], ['apple', 'banana']]
```

**Tuple:**  A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses. Tuples are immutable and can not be modified after creation. 

**Example:**

```python
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)
```

Output:

```markup
(('parrot', 'sparrow'), ('Lion', 'Tiger'))
```

## 5. Mapped data: dict
**dict:** A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.

**Example:**

```python
dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)
```

Output:
```markup
{'name': 'Sakshi', 'age': 20, 'canVote': True}
```

### Note"
* For String - use double quote
* Lists are mutable while Tuple are immutable (cannot change)
* dict - dictionary - are key-value pairs

### [Next Lesson>>](https://replit.com/@CodeWithHafsa/Day-06-Variables-and-Data-Types?v=1)