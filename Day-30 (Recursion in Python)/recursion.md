# Recursion in python
Recursion is the process of defining something in terms of itself.

## Python Recursive Function
In Python, we know that a function can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursive functions.

*Example* :
```python
# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(0) = 1      #by definition

# By logic:
# factorial(n) = n * factorial(n-1)

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3)) # 3*2*1 = 6
print(factorial(4)) #4*3*2*1 = 24
print(factorial(5)) #5*4*3*2*1 = 120
```

How it works:
```
for: print(factorial(5)) 

First go to if - not true
Then go to else:
Here: n * factorial(n-1)
Means:            5 * factorial (5-1) = 5 * factorial(4)
For factorial(4): 4 * factorial (4-1) = 5 * factorial(3)
For factorial(3): 3 * factorial (3-1) = 5 * factorial(2)
For factorial(2): 2 * factorial (2-1) = 5 * factorial(1)
So;               5*4*3*2*1 = 120

```
Output:
```
6
24
120
```

========================================================
*Example 02* :
```python
def factorial(num): 
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1)) 
  
# Driver Code 
num = 7; 
print("Number: ",num)
print("Factorial: ",factorial(num))
```

Output:
```
Number:  7
Factorial:  5040
```

## Quiz
Write a program to print fibonacci series.

Instructions:
* f0 = 0
* f1 = 1
* f2 = f1 + f0
* fn = f(n-1) + f(n-2)
* sequence = 0 1 1 2 3 5 8....

```python
a = int(input("Enter any number : "))  #tells the index number 

def fibonacci(n):
    if (n == 1 or n == 0):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

for i in range(a):
    print(fibonacci(i))
```

Output:
* If input = 7
```
0
1
1
2
3
5
8
```