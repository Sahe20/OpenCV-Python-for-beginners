from operator import __add__
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

# names = ['Abdullah', 'Ansu', 'Abraham'] #list literals
# characters = list ('aeiou')  # string literal -> list of characters
# print(names)
# print(characters)
# x = ['aeiou'] #list
# print(x)

# person = ('Alieu', 22, '123-456-789', '10-Monrovia')
# person2 = tuple (['Aisha', 19, '012-345-678', 'Brewerville'])
# print(person)
# print(person2)

                       #MATH OPERATIONS
A = (42 + 13) #addition
a = (42).__add__ (13)
# 42 - 13 #subtraction
# 42 * 13 #multiplication
# 42 / 13 #division
# 42 // 13 #floor division
# 42 % 13 #modulus
# 42 ** 13 #exponentiation
# 42 ** 0.5 #square root
# 42 ** (1/3) #cube root
print(a)
print(A)