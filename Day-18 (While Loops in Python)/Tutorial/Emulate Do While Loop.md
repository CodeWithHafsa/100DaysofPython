# Do-While loop in python
do..while is a loop in which a set of instructions will execute at least once (irrespective of the condition) and then the repetition of loop's body will depend on the condition passed at the end of the while loop. 
* It is also known as an exit-controlled loop.
* Do while loop - only in C/C++ and Java. Not in python.
* We use break statement in do while loop.

How it works:
* First execute - Donot check whether condition is true or false.
* Then, second time - Check whether condition is true or false.
* Then, third time - Executes only if the condition is true in second time or else came out of loop.

# How to emulate do while loop in python?
To create a do while loop in Python, you need to modify the while loop a bit in order to get similar behavior to a do while loop.

### Syntax:
```python
do {
    #loop body;
} while(condition)
```
---
*Example 1* :
```python
i = 0
while True:
  print(i)
  i = i +1
  if(i%10 == 0):
   break
```

Output:
```
0
1
2
3
4
5
6
7
8
9
```

---
*Example 2* :
```python 
while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break
```

Output
```
Enter a positive number: 1
1
Enter a positive number: 4
4
Enter a positive number: -1
-1
```

* Explanation:

This loop uses True as its formal condition. This trick turns the loop into an infinite loop. Before the conditional statement, the loop runs all the required processing and updates the breaking condition. If this condition evaluates to true, then the break statement breaks out of the loop, and the program execution continues its normal path.