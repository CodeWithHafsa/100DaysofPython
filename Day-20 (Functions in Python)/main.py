# a = 9
# b = 8
# gmean1 = (a*b) / (a+b)  #geometric mean
# print(gmean1)

# c = 8
# d = 7
# gmean1 = (c*d) / (c+d)  #geometric mean
# print(gmean1)



# def calculateGmean(a, b):
#   mean = (a*b) / (a+b)
#   print(mean)

# a = 9
# b = 8
# if (a>b):
#     print("First number is greater")
# else:
#     print("Second number is greater or equal")
# calculateGmean(a, b)
# # gmean1 = (a*b) / (a+b)  #geometric mean without function
# # print(gmean1)

# c = 8
# d = 7
# if (c>d):
#     print("First number is greater")
# else:
#     print("Second number is greater or equal")
# calculateGmean(c, d)
# # gmean1 = (c*d) / (c+d)   #geometric mean without function
# # print(gmean1)


def calculateGmean(a, b): #function for geometric mean
  mean = (a*b) / (a+b)
  print(mean)

def isGreater(a,b): #function for greater than
    if (a>b): #function definition(body)
        print("First number is greater")
    else:
        print("Second number is greater or equal")

def islesser(a,b):
    pass #means - pass this function (I will write it after)

a = 9
b = 8
calculateGmean(a, b)
isGreater(a,b)
# gmean1 = (a*b) / (a+b)  #geometric mean without function
# print(gmean1)

c = 8
d = 7
calculateGmean(c, d) #short form for geometric mean
isGreater(c,d)  #shortform for greater than
# gmean1 = (c*d) / (c+d)   #geometric mean without function
# print(gmean1)