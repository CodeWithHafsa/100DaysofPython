# Docstrings in python:
Python docstrings are the string literals that appear right after the definition of a function, method, class, or module. 

*Example* :
```python
def square(n): #function name
    '''Takes in a number n, returns the square of n'''  #docstring -special string
    print(n**2)   #function body
square(5)
print(square.__doc__)   #doc attribute
```

Output:
```
25
Takes in a number n, returns the square of n
```

NOTE: If we don't use doc attribute the only answer returns by the function, not the string. 

## Python Comments vs Docstrings

### Python Comments
Comments are descriptions that help programmers better understand the intent and functionality of the program. They are completely ignored by the Python interpreter.

### Python docstrings
While, Python docstrings are strings used right after the definition of a function, method, class, or module. They are used to document our code.\
We can access these docstrings using the __doc__ attribute.



## Key points:
* Comment does not effect on program output, while docstring might change output of program.
* Docstring always written right below the function name or right above the function body to make it valid string, as shown in above example.