# Introduction to Loops:
Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loops. Based on this loops are further classified into following main types; 
- for loop
- while loop 

* Using for loop:
```python
# using for loop:
for i in range(3):
    print(i)
```

Output:
```
0
1
2
```

#  Python while Loop:
As the name suggests, while loops execute statements while the condition is True. As soon as the condition becomes False, the interpreter comes out of the while loop. 

* Here interpretor means - python (which control/executes program)
---

* *Example 1*:\
Using while loop: Condition i<3:
```python
# using while looop:
i = 0
while(i<3):
    print(i)
    i = i + 1 #for every iteration i value increases+1

print("Done with the loop")
```

Output:
```
0
1
2
Done with the loop
```
---
* *Example 2* : \
Using while loop: Condition i<=3:
```python
# using while looop:
i = 0
while(i<=3):
    print(i)
    i = i + 1 #for every iteration i value increases+1

print("Done with the loop")
```

Output:
```
0
1
2
3
Done with the loop
```
---
* *Example 3* :\
Using while loop: Take input from user until i<=38:
```python
# using while looop:
i = int(input("Enter the number: "))
while(i<=38):
    i = int(input("Enter the number: "))
    print(i)

print("Done with the loop")
```

Output:
```
Enter the number: 9
9
Enter the number: 34
34
Enter the number: 38
38
Enter the number: 98
98
Done with the loop
```

## Decrimenting While Loop:
If the count variable is set to 5 which decrements after each iteration.

* *Example*:\
Decrimenting While Loop
```python
count = 5
while (count > 0):
  print(count)
  count = count - 1
```

Output:
```
5
4
3
2
1
```

Depending upon the while loop condition, we need to either increment or decrement the counter variable (the variable count, in our case) or the loop will continue forever.


# Else with While Loop
We can even use the else statement with the while loop. Essentially as soon as the while loop condition becomes False, the interpreter comes out of the while loop and the else statement is executed. 

*Example 1* :
```python
count = 5
while (count > 0):
  print(count)
  count = count - 1
else:
    print("I am inside else")
```

Output:
```
5
4
3
2
1
I am inside else
```
---
*Example 2* :
```python 
x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('counter is 0')
```

Output:
```
5
4
3
2
1
counter is 0
```