# Continue statement:
The continue statement skips the rest of the loop statements and causes the next iteration to occur.

*Example 1* :
```python
for i in range(12):
    if(i == 10): #print table of 5 till 10
        print("Skip the iteration")
        continue
    print("5 X", i, "=", 5 * (i)) 
```

Output:
```
5 X 0 = 0
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
Skip the iteration
5 X 11 = 55
```

*Example 2* :
```python
for i in [2,3,4,6,8,0]: 
    if (i%2!=0): #skips odd number
        continue
    print(i)
```

Output:
```
2
4
6
8
0
```