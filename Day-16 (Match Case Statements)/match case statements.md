# Match Case Statements:
A match statement will compare a given variable’s value to different shapes, also referred to as the pattern. The main idea is to keep on comparing the variable with all the present patterns until it fits into one.

The match case consists of three main entities :

1. The match keyword
2. One or more case clauses
3. Expression for each case

The case clause consists of a pattern to be matched to the variable, a condition to be evaluated if the pattern matches, and a set of statements to be executed if the pattern matches.

### Syntax:
```python
match variable_name:
            case ‘pattern1’ : //statement1
            case ‘pattern2’ : //statement2
            …            
            case ‘pattern n’ : //statement n
```

## Examples:
* *Example 1* :
```python
x = int(input("Enter the value of x: "))
# x is the variable to  match
match x:
    #  if x is 0:
    case 0:
       print("x is zero")
    # case with if-condition:
    case 4:
       print("case is 4")
    case _:
       print(x) #default case
```

Output:
* If input = 5
```
Enter the value of x: 5
5
```
---
* if input = 4
```
Enter the value of x: 4
case is 4
```
---
* if input = 0
```
Enter the value of x: 0
x is zero
```
=========================================================
* *Example 2* :
```python
x = int(input("Enter the value of x: "))
# x is the variable to  match
match x:
    #  if x is 0:
    case 0:
       print("x is zero")
    # case with if-condition:
    case 4:
       print("case is 4")
    case _ if x!=90:
       print(x, "is not 90") 
    case _ if x!=80:
       print(x, "is not 80") 
    case _ :
       print(x) #default case
```

* If any case matches one time, than python doesnot match other cases. It just returns result.

Output:
* if input = 56
```
Enter the value of x: 56
56 is not 90
```
---
* if input = 90
```
Enter the value of x: 90
90 is not 80
```
=========================================================
* *Example 3* :
```python
x = 4
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    # Empty case with if-condition
    case _ if x < 10:
        print("x is < 10")
    # default case(will only be matched if the above cases were not matched)
    # so it is basically just an else:
    case _:
        print(x)
```

Output:
```
x % 2 == 0 and case is 4
```


## Key Points:
* Switch Case Statements in C/C++ = Match Case Statements in python
* break statement - use in C/C++ 
* Default case is a kind of 'else statement'