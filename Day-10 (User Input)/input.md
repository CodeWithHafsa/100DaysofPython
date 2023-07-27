# Taking User Input in python
* Use input() function.
* This input function gives a return value as string/character hence we have to pass that into a variable

**Example#1**
```python
a = input("Enter your name: ")
print("My name is", a)
```

Output:
```markup
Enter your name: Hafsa #name given by user
My name is Hafsa #print by python
```
* Python input() function - takes input as a string. So we have to define its data type(i.e. it is integar/float etc)
* Or it can be resolved by 'typecasting'

**Example#2**
```python
x = input("Enter first number: ") #string
y = input("Enter first number: ") #string
print (x + y) #print as it it as 'string' i.e. 458
print(int(x) + int(y)) #typecasting - convert into integar than add i.e. 53
```

Output:
```markup
Enter first number: 45    #given by user
Enter second number: 8  #given by user
458    #print by python 
53     #print by python
```
### [Next Lesson>>](https://replit.com/@CodeWithHafsa/Day-11-Strings?v=1)
