# Comments, Escape Sequences & Print Statement
### Comments
Comment & Print Statements
```python
# Hey, Do not remove this line.
# Author: Hafsa
# Course: 100DaysofCode
print("This is a print statement \nThis is a new line")
print("Hello World!!!") #Printing Hello World
```

Output:
```
This is a print statement
This is a new line
Hello World!!!
```
___

### Escape Sequence Characters
To insert characters that cannot directly used in a string, we use 'escape sequence character'

* <ins> <span style="color: orange;">*Back-Slash Double quote:*</span>
```python
print("This is a \"print statement\" and this is a new line")
```

Output:
```
This is a "print statement" 
and this is a new line
```

* <ins> <span style="color: orange;">*Back-Slash Single quote:*</span>
```python 
print('This is\' a \"print statement\" and this is a new line')
```

Output:
```
This is a' "print statement
and this is a new line
```
___

### Print Statement:
We can write mutiple words in single print statement.
* <ins> <span style="color: orange;">*Separator:*</span>
```python
print("Hey", 6, 7, sep"~" )
```

Output:
```
Hey~6~7
```

* <ins> <span style="color: orange;">*End:*</span>
```python
print("Hey", 6, 7, sep"~", end="009\n")
print("Hafsa")
```

Output:
```
Hey~6~7~009
Hafsa
```

#### Note:
* \n - is a "escape sequence character" - Used for "new line"
* '#' - Used to write comment - that doesnot execure
* Triple single quote or Triple double quote - can also used to comment multiple lines

### [Next Lesson>>](https://replit.com/@CodeWithHafsa/Day-06-Variables-and-Data-Types?v=1)