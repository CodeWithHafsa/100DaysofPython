# l = [1, 2, 4, 6]
# print(l)
# l.append(7) #append
# l.sort() #sort in ascending order
# l.sort(reverse=True) #sort in descending order
# print(l)

# l.reverse() #reverse original list
# print(l.index(1)) #returns first occurrece

# l = [11, 45, 1, 2, 4, 6, 1, 1]
# print(l.count(1)) #count how many times '1' came in list
# print(l)

# l = [11, 45, 1, 2, 4, 6, 1, 1]
# print(l)
# m = l
# m[0] = 0 #it makes changes in both m and l lists.
# print(l)

# l = [11, 45, 1, 2, 4, 6, 1, 1]
# print(l)
# m = l.copy()
# m[0] = 0 
# print(l) #it only changes m list.

# l = [11, 45, 1, 2, 4, 6, 1, 1]
# print(l)
# l.insert(1, 899) #at index[1] value changes to 899.
# print(l)

# l = [11, 45, 1, 2, 4, 6, 1, 1]
# m =[900, 1000, 1100]
# l.extend(m) #open m and add at the end of l
# print(l)

l = [11, 45, 1, 2, 4, 6, 1, 1]
m =[900, 1000, 1100]
k = l + m
print(k)