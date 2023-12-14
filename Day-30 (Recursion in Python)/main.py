# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(3)) # 3*2*1 = 6
# print(factorial(4)) #4*3*2*1 = 24
# print(factorial(5)) #5*4*3*2*1 = 120


a = int(input("Enter any number : "))

def fibonacci(n):
    if (n == 1 or n == 0):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(a)

# for i in range(a):
#     print(fibonacci(i))