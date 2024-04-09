import sys
#print ("Hello, World!")
#mutable and immutable object ex:

# my_list = [1,2,3]
# print (id(my_list))  

# my_list.append(4)
# print(id(my_list)) # mutable obj

# my_tuple = (1,2,3)
# print(id(my_tuple)) 

# my_tuple += (4,)
# print(id(my_tuple)) #immutable obj

#reference count ex:
# a=300 
# print(sys.getrefcount(a))

#Literals 

# name = 'Musa \N{GRINNING FACE}' #literal 
# age_string = str(40) #str constructor, coverts integer to str
# print(name)

# age = 23 # integer literal (int)
# cost = 9.9 # float literal (float)
# loc = 1+8j # complex literal (complex)
# print (type(age), type(cost), type(loc))

names = ['Abdullah', 'Ansu', 'Abraham'] #list literals
characters = list ('aeiou')  # string literal -> list of characters
print(names)
print(characters)
x = ['aeiou'] #list
print(x)

