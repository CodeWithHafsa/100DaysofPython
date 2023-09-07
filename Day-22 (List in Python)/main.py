# marks = [3, 5, 6, "Harry", True]
# print(marks)
# print(type(marks))
# print(marks[0])  #indexing
# print(marks[1])  #indexing
# print(marks[2])  #indexing
# print(marks[3])  #indexing
# print(marks[4])  #indexing

# marks = [3,5,6,"Harry",True]
# print(marks[-3]) # Negative index
# print(marks[len(marks)-3 ]) # Positive index
# print(marks[5-3]) # Positive index
# print(marks[2]) # Positive index

# marks = [3, 5, 6, "Harry", True]
# if 7 in marks:
#     print("Yes")
# else:
#     print("No")

# if "arry" in "Harry":
#     print("Yes")
# else:
#     print("No")

# marks = [3, 5, 6, "Harry", True, 6, 7, 2, 32, 345, 23]
# print(marks)
# print(marks[1:-1]) #len=11, 11-1=10 #print(marks[1:10])
# print(marks[1:8])
# print(marks[1:8:3])

# lst = [i for i in range(4)]
# print(lst)

# lst = [i*i for i in range(4)]
# print(lst)

lst = [i*i for i in range(10) if i%2==0] #if i is divisible by 2 then show number
print(lst)