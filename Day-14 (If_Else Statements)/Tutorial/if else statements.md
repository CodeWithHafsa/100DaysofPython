# if-else Statements:
Sometimes the programmer needs to check the evaluation of certain expression(s), whether the expression(s) evaluate to True or False. If the expression evaluates to False, then the program execution follows a different path than it would have if the expression had evaluated to True.

*Example: if-else statement* :
```python
a = int(input("Enter your age: "))
print("Your age is: ", a)

if(a>18):
    print("You can drive")
    print("Yes")
else:
    print("You cannot drive")
    print("No")
print("Yay!") #no indentation here - means it prints every time
```

Output:
* if input = 9
```
Enter your age: 9
Your age is:  9
You cannot drive
No
Yay!
```
---
* if input = 76
```
Enter your age: 76
Your age is:  76
You can drive
Yes
Yay!
```
=========================================================

*Example: Without indentation*
```python
a = int(input("Enter your age: "))
print("Your age is: ", a)

if(a>18):
    print("You can drive")
    print("Yes")
else:
    print("You cannot drive")
    print("No")
    print("Yay!") #indentation here - means it only prints in case of else
```

Output:
* if input = 9
```
Enter your age: 9
Your age is:  9
You cannot drive
No
```
---
* if input = 76
```
Enter your age: 73
Your age is:  73
You can drive
Yes
Yay!
```
========================================================

*Example* :
```python
applePrice = 210
budget = 200
if (applePrice <= budget):
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")
```

Output:
```
Alexa, do not add Apples to the cart.
```

# elif Statements:
Sometimes, the programmer may want to evaluate more than one condition, this can be done using an elif statement.

*Example 1* :
```python
applePrice = 10
budget = 200
if (budget - applePrice):
    print("Alexa, add 1 kg Apples to the cart.")
elif(budget - applePrice > 70):
    print("Its okay you can buy")
else:
    print("Alexa, do not add Apples to the cart.")
```

Output:
```
Alexa, add 1 kg Apples to the cart.
```
========================================================
*Example 2* :
```python
num = int(input("Enter the value of num: "))
if (num < 0):
    print("Number is negative.")
elif (num == 0):
    print("Number is Zero.")
elif (num == 999):
    print("Number is Special.")
else:
    print("Number is positive.")

print("I am happy now")
```

Output:
* if input = 7
```
Enter the value of num: 7
Number is positive.
I am happy now
```

* if input = -8
```
Enter the value of num: -8
Number is negative.
I am happy now
```

* if input = 0
```
Enter the value of num: 0
Number is Zero.
I am happy now
```

* if input = 999
```
Enter the value of num: 999
Number is Special.
I am happy now
```

# Nested if Statements:
We can use if, if-else, elif statements inside other if statements as well. \
*Example* :
```python
num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")
```

Output:
```
Number is between 11-20
```

## Key Points:
* Indentation in python - means we  enter in a 'block' line.
* Level of indentation - means under indentation there is another indentation.

### [Next Lesson](https://replit.com/@CodeWithHafsa/Good-Morning-Sir-15-and-26)