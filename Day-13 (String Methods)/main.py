a = "Hafsa"
print(len(a))
print(a.upper())
print(a.lower())

str2 = " Silver Spoon "
print(str2.strip)
a = "Hafsa!!!"
print(a.rstrip("!"))
b = "!!Hafsa!!!!" #it doesnot remove trailing characters that are at the start of string.
print(b.rstrip("!"))

a = "Hafsa learns coding"
print(a.replace("Hafsa", "John"))

a = "Hafsa John Harry" #here where is space present, it converts them into list
print(a.split(" "))

blogHeading = "introduction to python" #here 'introduction' 'i' is in lowercase converts into uppercase. 
print(blogHeading.capitalize)
blogHeading2 = "introduction tO python" #here 'tO' 'O' is in uppercase converts into lowercase.
print(blogHeading2.capitalize)

str1 = "Welcome to the Console!!!"
print(len(str1)) #len of above string is
print(str1.center(20)) #it adds 20 spaces before string
str1 = "Welcome to the Console!!!"
print(str1.center(50, "."))

a = "Hafsa!! John Harry Hafsa" 
print(a.count("Hafsa")) #it counts how many times 'h\Hafsa' occur in string

str1 = "Welcome to the Console !!!" 
print(str1.endswith("!!!")) #it tells that whether or not strings end with '!'

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10)) #it tells that whether or not string b/w 4 and 10 index i.e. "ome to" endswith 'to'

str1 = "He's name is Dan. He is an honest man." 
print(str1.find("is")) #it tells index of where 'is' is present.
str1 = "He's name is Dan. He is an honest man."
print(str1.find("Daniel")) #if it doesnot find given string retrurn -1

str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Daniel")) #if it doesnot find given string retrurn error

