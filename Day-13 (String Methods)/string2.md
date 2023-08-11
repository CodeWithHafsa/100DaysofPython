More String Methods:

26. format() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  34. maketrans()  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 42. casefold()
27. format_map() &nbsp;&nbsp;&nbsp; 35. partition() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 43. encode()
28. isascii() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 36. rfind() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 44. exapndtabs()
29. isdecimal() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 37. rindex() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;45. isnumeric()
30. isdigit() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 38. rpartition() 
31. isidentifier() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 39. splitlines() 
32. join() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;40. translate()
33. ljust() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 41.zfill()

## 26. format():
The format() method - Formats given values in a string

*Example*
```python
#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("John",36)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("John",36)
```

Output:
```markup
My name is John, I'm 36
My name is John, I'm 36
My name is John, I'm 36
```

## 27. format_map():
The format_map() method - Formats specified given values in a string.

*Example*
```python
point = {'x':4,'y':-5}
print('{x} {y}'.format_map(point))

point = {'x':4,'y':-5, 'z': 0}
print('{x} {y} {z}'.format_map(point))
```

Output:
```
4 -5
4 -5 0
```
___

## 28. isascii():
The isascii() method - Returns True if all the characters are ascii characters (a-z) or (A-Z) or (0-9).

*Example*
```python
txt = "Company123"
x = txt.isascii()
print(x)
```

Output:
```
True
```

## 29. isdecimal():
The isdecimal() method - Returns True if all the characters are decimals (0-9). 

This method can also be used on unicode objects. 

*Example#1*
```python
txt = "1234"
x = txt.isdecimal()
print(x)
```

Output:
```
True
```
---
*Example#2*
```python
a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G

print(a.isdecimal())
print(b.isdecimal())
```

Output:
```
True
False
```

## 30. isdigit():
The isdigit() method returns True if all the characters are digits, otherwise False.

Exponents, like ², are also considered to be a digit.

*Example#1*
```python
txt = "50800"
x = txt.isdigit()
print(x)
```

Output:
```
True
```
---
*Example#2*
```python
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²

print(a.isdigit())
print(b.isdigit())
```

Output:
```
True
True
```

## 31. isidentifier():
The isidentifier() method - Returns True if the string is a valid identifier, otherwise False.

A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.

*Example*
```python
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())
```

Output:
```
True
True
False
False
```

## 32. join():
The join() method - Takes all items in an iterable and joins them into one string.

A string must be specified as the separator.

*Example#1*
```python
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)
```

Output:
```
John#Peter#Vicky
```

*Example#2*
```python
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)
```

Output:
```
nameTESTcountry
```

## 33. ljust():
The ljust() method - will left align the string, using a specified character (space is default) as the fill character.

*Example#1*
```python
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")
```

Output:
```
banana               is my favorite fruit.

'Note: In the result, there are actually 14 whitespaces to the right of the word banana.'
```

*Example#2*
```python
txt = "banana"
x = txt.ljust(20, "O")
print(x)
```

Output:
```
bananaOOOOOOOOOOOOOO
```

## 34. maketrans():
The maketrans() method - Returns a mapping table that can be used with the translate() method to replace specified characters.

*Example#1*

```python
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))
```

Output:
```
​Hello Pam!
```
* Use a mapping table to replace many characters:

*Example#2*
```python
txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y)
print(txt.translate(mytable))
```

Output:
```
Hi Joe!
```

* The third parameter in the mapping table describes characters that you want to remove from the string:

*Example#3*

```python
txt = "Good night Sam!"
x = "mSa"  
y = "eJo"
z = "odnght"
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable))
```

How it works:
```
Here:
'm' replace with 'e'
'S' replace with 'J'
'a' replace with 'o'
And:
'odnght' - i remaining in string.
```

Output:
```
G i Joe!
```

## 35. partition():
The partition() method - Searches for a specified string, and splits the string into a tuple containing three elements.

* The first element contains the part before the specified string.
* The second element contains the specified string.
* The third element contains the part after the string.

*Example#1*

```python
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)
```

Output:
```
('I could eat ', 'bananas', ' all day')
```

*Example#2*

```python
txt = "I could eat bananas all day"
x = txt.partition("apples")
print(x)
```

Output:
```
('I could eat bananas all day', '', '')
```

## 36. rfind():
* The rfind() method finds the last occurrence of the specified value.
* The rfind() method returns -1 if the value is not found.
* The rfind() method is almost the same as the rindex().

*Example#1*
```python
txt = "Mi casa, su casa." 
x = txt.rfind("casa") #check last occurence of 'casa'
print(x)
```

Output:
```
12
```

*Example#2*
```python
txt = "Hello, welcome to my world."
x = txt.rfind("e") #check last occurrence of 'e'
print(x)
```

Output:
```
13  
```

*Example#3*
```python
txt = "Hello, welcome to my world."
x = txt.rfind("e", 5, 10) #index of 'e' between 5 and 10 index.
print(x)
```

Output:
```
8
```

## 37. rindex():
* The rindex() method finds the last occurrence of the specified value.
* The rindex() method raises an exception if the value is not found.
* The rindex() method is almost the same as the rfind() method. 

*Example#1*
```python
txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)
```

Output:
```
12
```

*Example#2*
```python
txt = "Hello, welcome to my world."
x = txt.rindex("e", 5, 10) #index of 'e' between 5 and 10 index.
print(x)
```

Output:
```
8
```

## 38. rpartition():
The rpartition() method searches for the last occurrence of a specified string, and splits the string into a tuple containing three elements.

* The first element contains the part before the specified string.
* The second element contains the specified string.
* The third element contains the part after the string.

*Example*
```python
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)
```

Output:
```
('I could eat bananas all day, ', 'bananas', ' are my favorite fruit')
```

*Example#2*
```python
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("apples")
print(x)
```

Output:
```
('', '', 'I could eat bananas all day, bananas are my favorite fruit')
```

## 39. splitlines():
The splitlines() method splits a string into a list. The splitting is done at line breaks.

*Example#1*
```python
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines() #here \n does not came in return
print(x)
```

Output:
```
['Thank you for the music', 'Welcome to the jungle']
```

*Example#2*
```python
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines(True) #here \n cames in return
print(x)
```

Output:
```
['Thank you for the music\n', 'Welcome to the jungle']
```

## 40. translate():
The translate() method returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table.

* Use the maketrans() method to create a mapping table.
* If a character is not specified in the dictionary/table, the character will not be replaced.
* If you use a dictionary, you must use ascii codes instead of characters.

*Example#1*
```python
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))
```

Output:
```
Hello Pam!
```

*Example#2*
```python
txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y)
print(txt.translate(mytable))
```

Output:
```
Hi Joe!
```

## 41. zfill():
The zfill() method - Adds zeros (0) at the beginning of the string, until it reaches the specified length.

If the value of the len parameter is less than the length of the string, no filling is done.

*Example#1*
```python
txt = "50"
x = txt.zfill(10)
print(x)
```

Output:
```
0000000050
```

*Example#2*
```python
a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))
```

Output:
```
00000hello
welcome to the jungle
000010.000
```

## 42. casefold():
The casefold() method - Returns a string where all the characters are lower case.

*Example*
```python
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)
```

Output:
```
hello, and welcome to my world!
```

## 43. encode():
The encode() method - Encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.

*Example#1*
```python
txt = "My name is Ståle"
x = txt.encode()
print(x)
```

Output:
```
b'My name is St\xc3\xe5le'
```

*Example#2*
```python
txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
```

Output:
```
b'My name is St\\xe5le'
b'My name is Stle'
b'My name is St\\N{LATIN SMALL LETTER A WITH RING ABOVE}le'
b'My name is St?le'
b'My name is Ståle'
```

## 44. expandtabs
The expandtabs() method - Sets the tab size to the specified number of whitespaces.

*Example#1*
```python
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)
```

Output:
```
H e l l o
```

*Example#2*
```python
txt = "H\te\tl\tl\to"

print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))
```

Output:
```
H       e       l       l       o
H       e       l       l       o
H e l l o
H   e   l   l   o
H         e         l         l         o
```

## 45. isnumeric
The isnumeric() method - Returns True if all the characters are numeric (0-9), otherwise False.

* Exponents, like ² and ¾ are also considered to be numeric values.
* "-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and the - and the . are not.

*Example#1*
```python
txt = "565543"
x = txt.isnumeric()
print(x)
```

Output:
```
True
```

*Example#2*
```python
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²
c = "10km2"
d = "-1"
e = "1.5"

print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print(e.isnumeric())
```

Output:
```
True
True
False
False
False
```