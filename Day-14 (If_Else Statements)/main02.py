# elif statements:

# applePrice = 10
# budget = 200
# if (budget - applePrice):
#     print("Alexa, add 1 kg Apples to the cart.")
# elif(budget - applePrice > 70):
#     print("Its okay you can buy")
# else:
#     print("Alexa, do not add Apples to the cart.")

# num = int(input("Enter the value of num: "))
# if (num < 0):
#     print("Number is negative.")
# elif (num == 0):
#     print("Number is Zero.")
# elif (num == 999):
#     print("Number is Special.")
# else:
#     print("Number is positive.")
    
# print("I am happy now")

# nested if
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
