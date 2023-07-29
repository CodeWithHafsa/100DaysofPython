# String in Python
Anything enclosed in single or double quote is known as "string". It is a sequence of array or textual data.

**Example**
```python
name = "Hafsa"
friend = "Rohan"
anotherFriend = 'Harry'
print("Hello, ", name)
```

Output:
```markup
Hafsa
Rohan
Harry
Hello, Hafsa
```

## Quotation marks in between string

**Example**
```python
apple = "He said, \"I want to eat an apple" #use escape sequence, or
apple = 'He said, \"I want to eat an apple' #string can enclose in single quote
print(apple)
```

Output:
```markup
He said, "I want to eat an apple
He said, "I want to eat an apple
```

## Multilines string
* Multiple lines should enclose in - triple single quote or triple double quote.

**Example**
```python
apple = '''He said,
Hi Hafsa
hey I am good
"I want to eat an apple'''
```

Output:
```markup
He said,
Hi Hafsa
hey I am good
"I want to eat an apple
```

## Indexing
It is ' acessing chracters of a string.
In python - string is like an array of chracyers (not exactly)

```python
name = "Hafsa"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
#print(name[5])   #throws index error - b/c there is nothing at 5.
```

How it works: 
```
Index# 0 1 2 3 4 5
       H a f s a
```

Output:
```markup
H
a
f
s
a
```

## Looping through the string
for loop - characters print all the characters of string

```python
name = "Hafsa"
for character in name:
    print(character)
```

Ouput:
```markup
H
a
f
s
a
```

### [Next Lesson>>](https://replit.com/@CodeWithHafsa/Day-12-String-Slicing-and-Operators?v=1)
