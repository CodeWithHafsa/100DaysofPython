# tup = (1, 5, 6)
# print(type(tup), tup)

# tup = [1, 2, 76, 342, 32, "green", True]  #tuple
# print(type(tup), tup)

# Indexing
# tup = (1,  2,  76,  342, 32, "green", True)
#    [0] [1]  [2]  [3]  [4]   [5]    [6]

# print(len(tup)) #output: 7
# print(tup[0])  #positive indexing
# print(tup[-1]) #negative indexing= len(tup) -1 => 7-1 =6
# print(tup[2])
# print(tup[3])

# Check for item
# tup = (1,  2,  76,  342, 32, "green", True)
# if 342 in tup:
#     print("Yes 342 is present in tuple")

tup = (1, 2, 76, 342, 32, "green", True)
tup2 = tup[1:4] #slicing
print(tup2) # returns a new tuple