# String formatting in python
String formatting can be done in python using the format method. It is used for string concatination. 

NOTE: This method is not appropriate for longer programs. 

*Example 01* :
```python
text = "Hey my name is {} and I am from {}"
country = "Pakistan"
name = "Hafsa"

print(text.format(name, country))
```

Output:
```
Hey my name is Hafsa and I am from Pakistan
```
========================================================
*Example 02* :
```python
text = "Hey my name is {1} and I am from {0}"
country = "Pakistan"
name = "Hafsa"

print(text.format(country, name)) #output: Hey my name is Pakistan and I am from Hafsa.

# To fix the error we use indexing in text string.
```

Output:
```
Hey my name is Hafsa and I am from Pakistan
```
========================================================
*Example 03*:
```python
txt = "For only {price:.2f} dollars!" #.2f means takes only two decimal places
print(txt.format(price = 49.0009))
```

Output:
```
For only 49.00 dollars!
```

# f-strings in python
It is a new string formatting mechanism introduced by the PEP 498. It is also known as Literal String Interpolation or more commonly as F-strings (f character preceding the string literal). The primary focus of this mechanism is to make the interpolation easier.

When we prefix the string with the letter 'f', the string becomes the f-string itself. The f-string can be formatted in much same as the str.format() method. The f-string offers a convenient way to embed Python expression inside string literals for formatting.

*Example 01* :
```python
country = "Pakistan"
name = "Hafsa"
print(f"Hey my name is {name} and I am from {country}")
```

Output:
```
Hey my name is Hafsa and I am from Pakistan
```
========================================================
*Example 02* :
```python
price = 49.0009
txt = f"For only {price:.2f} dollars!" #.2f means takes only two decimal places
print(txt)
```

Output:
```
For only 49.00 dollars!
```
========================================================
*Example 03* : *To print curly brackets in f-string*
```python
country = "Pakistan"
name = "Hafsa"
print(f"Hey my name is {{name}} and I am from {{country}}") #use double curly brackets
```

Output:
```
Hey my name is {Hafsa} and I am from {Pakistan}
```
========================================================
*Example 04* :
```python
val = 'Geeks'  
print(f"{val}for{val} is a portal for {val}.")  
name = 'Tushar'  
age = 23  
print(f"Hello, My name is {name} and I'm {age} years old.")  
```
In the above code, we have used the f-string to format the string. It evaluates at runtime; we can put all valid Python expressions in them.

========================================================
*Example 05* : *We can use it in a single statement as well.*

```python
print(f"{2 * 30}")
```

Output:
```
60
```