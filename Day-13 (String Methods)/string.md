# String Methods in Python
Python provides a set of built-in methods that we can use to alter and modify the strings.
Strings are immutable - it means that it creates a new string, that means it doesnot change existing string. 

Methods:
1. upper() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 11. startswith() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 21. islower()
2. lower() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 12. find() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 22. swapcase() 
3. strip() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 13. index() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;23. title() 
4. rstrip() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 14. isalnum() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;24. replace()
5. lstrip() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 15. isalpha() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 25.capitalize()
6. split()  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  16. islower() 
7. rsplit() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 17. isprintable() 
8. center() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 18. isspace() 
9. count()  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 19. istitle() 
10. endswith() &nbsp;&nbsp;&nbsp;&nbsp; 20. isupper() 

## 1. upper() :
The upper() method converts a string to upper case/ capital alphabets.

## 2. lower()
The lower() method converts a string to lower case / small alphabets.

*Example*

```python
a = "Hafsa"
print(len(a))
print(a.upper())
print(a.lower())
```

Output:
```markup
5
HAFSA
hafsa
```

## 3. strip() :
The strip() method removes any white spaces before and after the string.

## 4. rstrip() : 
The rstrip() removes trailing characters (!!!) that are at the end of string.

## 5. lstrip() : 
The lstrip() method -  removes trailing characters (!!!) that are at the start of string.

* *Strip: Example*

```python
str2 = " Silver Spoon "
print(str2.strip)
```

Output:
```markup
Silver Spoon
``` 

* *R-strip: Example*

```python
a = "Hafsa!!!"
print(a.rstrip("!"))
b = "!!Hafsa!!!!" #it doesnot remove trailing characters that are at the start of string.
print(b.rstrip("!"))
```

Output:
```markup
Hafsa
!!Hafsa
```


* *lstrip: Example*

```python
b = "!!Hafsa!!!!" #it doesnot remove trailing characters that are at the end of string.
print(b.lstrip("!"))
```

Output:
```markup
Hafsa!!!!
```

## 6. split() :
The split() method splits the given string at the specified instance and returns the separated strings as 'list items'.

*Example*
```python
a = "Hafsa John Harry" #here where is space present, it converts them into list
print(a.split(" "))
```

Output:
```markup
['Hafsa', 'John', 'Harry']
```
## 7. rsplit():
The rsplit() method splits a string into a list, starting from the right.

If no "max" is specified, this method will return the same as the split() method.

*Example#1*
```python
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)
```

Output:
```
['apple', 'banana', 'cherry']
```

*Example#2*
```python
txt = "apple, banana, cherry" # setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 1)
print(x)
# note that the result has only 2 elements "apple, banana" is the first element, and "cherry" is the last.
```

Output:
['apple, banana', 'cherry']

## 8. center() : 
The center() method aligns the string to the center as per the parameters given by the user.

**Example**

```python
str1 = "Welcome to the Console!!!"
print(len(str1)) #len of above string is
print(str1.center(20)) #it adds 20 spaces before string
```

Output:
```markup
            Welcome to the Console!!! #len of this string is '20'
```

We can also provide padding character. It will fill the rest of the fill characters provided by the user.

**Example**

```python
str1 = "Welcome to the Console!!!"
print(str1.center(50, "."))
```
### Output:
```markup
............Welcome to the Console!!!.............
```

## 9. count() :
The count() method returns the number of times the given value has occurred within the given string.

**Example**
```python
a = "Hafsa!! John Harry Hafsa" 
print(a.count("Hafsa")) #it counts how many times 'h\Hafsa' occur in string
```

Output:
```markup
2
```

## 10. endswith() : 
The endswith() method checks if the string ends with a given value. If yes then return True, else return False. 

**Example**
```python
str1 = "Welcome to the Console !!!" 
print(str1.endswith("!!!")) #it tells that whether or not strings end with '!'
```

Output:
```markup
True #it is boolean data type
```

* We can even also check for a value in-between the string by providing start and end index positions.

**Example**

```python
str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10)) #it tells that whether or not string b/w 4 and 10 index i.e. "ome to" endswith 'to'
```
Output:
```markup
True
```

## 11. startswith() :
The endswith() method - checks if the string starts with a given value. If yes then return True, else return False. 

*Example*
```python
str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))
```

Output:
```
True
 ```

## 12. find() : 
The find() method searches for the first occurrence of the given value and returns the index where it is present. 

If given value is absent from the string then return -1.

*Example*

```python
str1 = "He's name is Dan. He is an honest man." 
print(str1.find("is")) #it tells index of where 'is' is present.
```
Output:
```markup
10
```

As we can see, this method is somewhat similar to the index() method. The major difference being that index() raises an exception if value is absent whereas find() does not.

*Example*
```python
str1 = "He's name is Dan. He is an honest man."
print(str1.find("Daniel")) #if it doesnot find given string retrurn -1
```
Output:
```markup
-1
 ```


## 13. index() :
The index() method searches for the first occurrence of the given value and returns the index where it is present. 

If given value is absent from the string then raise an exception.

*Example*
```python
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))
```
Output:
```markup
13
 ```
 
As we can see, this method is somewhat similar to the find() method. The major difference being that index() raises an exception if value is absent whereas find() does not.

*Example*
```python
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Daniel")) #if it doesnot find given string retrurn error
```
Output:
```markup
ValueError: substring not found
 ```

## 14. isalnum() :
The isalnum() method - returns True only if the entire string only consists of A-Z, a-z, 0-9. 

If any other characters or punctuations are present, then it returns False.

*Example*
```python
str1 = "WelcomeToTheConsole"
print(str1.isalnum())
```
Output:
```
True
 ```

## 15. isalpha() :
The isalnum() method - returns True only if the entire string only consists of A-Z, a-z. 

If any other characters or punctuations or numbers(0-9) are present, then it returns False.

*Example#1*
```python
str1 = "Welcome"
print(str1.isalpha())
```

Output:
```
True
 ```

*Example#2*
```python
str1 = "Welcome00"
print(str1.isalpha())
```

Output:
```
False
 ```

## 16. islower() :
The islower() method returns True if all the characters in the string are lower case, else it returns False. 

*Example*
```python
str1 = "hello world"
print(str1.islower())
```
Output:
```
True
 ```

## 17. isprintable() :
The isprintable() method - returns True if all the values within the given string are printable, if not, then return False.

*Example#1*
```python
str1 = "We wish you a Merry Christmas"
print(str1.isprintable())
```

Output:
```
True
 ```

*Example#2*
```python
str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable()) 
```

Output:
```
False #here\n is non-printable character that's why it returns false
 ``` 

## 18. isspace() :
The isspace() method - returns True only and only if the string contains white spaces, else returns False.

*Example*
```python
str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())
```

Output:
```
True
True
 ```

## 19. istitle() : 
The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.

*Example#1*
```python
str1 = "World Health Organization" 
print(str1.istitle())
```

Output:
```
True
 ```

*Example#2*
```python
str2 = "To kill a Mocking bird"
print(str2.istitle())
```
Output:
```
False
 ```

## 20. isupper() :
The isupper() method - returns True if all the characters in the string are upper case, else it returns False. 

## 21. islower 
The islower() method - Returns True if all the characters are in lower case, otherwise False.

Numbers, symbols and spaces are not checked, only alphabet characters.

* *isupper: Example*
```python
str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())
```
Output:
```
True
 ```

* *islower(): Example*
```python
a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"

print(a.islower())
print(b.islower())
print(c.islower())
```

Output:
```
False
True
False
```

## 22. swapcase() : 
The swapcase() method - changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.

*Example*
```python
str1 = "Python is a Interpreted Language" 
print(str1.swapcase()) #convert uppercase to lowercae & lowercase to uppercase.
```

Output:
```
pYTHON IS A iNTERPRETED lANGUAGE
 ```

### 23. title() :
The title() method capitalizes each letter of the word within the string.

*Example*
```python
str1 = "He's name is Dan. Dan is an honest man." #all word first character become capital
print(str1.title())
```

Output:
```
He'S Name Is Dan. Dan Is An Honest Man.
```

## 24. replace() : 
The replace() method replaces all occurences of a string with another string.

*Example#1*

```python
a = "Hafsa learns coding"
print(a.replace("Hafsa", "John"))
```

Output:
```markup
John learns coding
```

*Example#2*

```python
txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 2)
print(x)
```

Output:
```
three three was a race horse, two two was one too."
```

## 25. capitalize() : 
The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. 

The string has no effect if the first character is already uppercase.

*Example*

```python
blogHeading = "introduction to python" #here 'introduction' 'i' is in lowercase converts into uppercase. 
print(blogHeading.capitalize)
blogHeading2 = "introduction tO python" #here 'tO' 'O' is in uppercase converts into lowercase.
print(blogHeading2.capitalize)
```

Output:
```markup
Introduction to python
Introduction to python
```