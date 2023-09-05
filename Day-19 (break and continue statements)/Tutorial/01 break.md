# break statement
The break statement enables a program to skip over a part of the code. A break statement terminates the very loop it lies within.

*Example* :
```python
for i in range(12):
    if(i == 10): #print table of 5 till 10
        break
    print("5 X", i+1, "=", 5 * (i+1)) 

print("Out of the Loop")
```

Output:
```
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
Out of the Loop
```


## Key Points:
* loops works as iteration by iteration:
   * If we want to exit loop at particular loop - we use 'break statement'
   * If we want to skip iteration (code of loop body) at particular iteration - we use 'continue statement'