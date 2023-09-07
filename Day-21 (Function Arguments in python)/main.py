# def average(a=9, b=1): #default arguments
#     print("The average is ", (a+b)/2)
# average()

# def average(a=9, b=1): #keyword arguments
#     print("The average is ", (a+b)/2)
# average(b=9, a=21) #here order of value doesnot matters

# def average(a, b, c=1): #required arguments
#     print("The average is ", (a + b + c) / 2)
# average(5,6) 

# def average(*numbers):  #variable length argument - Arbitrary argument
#     #print(type(number)) # tuple
#     sum = 0 #initialize
#     for i in numbers:
#         sum = sum + i
#         print("Average is: ", sum/len(numbers))

# # average(5,6)
# average(5, 6, 7, 1)


# def name(**name):  #variable length argument - Keyword arbitrary argument
#     print("Hello,", name["fname"], name["mname"], name["lname"])

# name(mname = "Buchanan", lname = "Barnes", fname = "James")

def average(*numbers):   #return statement
    sum = 0 #initialize
    for i in numbers:
        sum = sum + i
        return sum/len(numbers)

c = average(5, 6, 7, 1)
print(c)   #return function stores value and save it in varaible