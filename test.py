import math
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
# A = (42 + 13) #addition
# a = (42).__add__ (13)
# A = 42 - 13 #subtraction
# a = (42). __sub__ (13)
# A = 42 * 13 #multiplication
# a = (42).__mul__ (13)
# A = 42 / 13 #division
# a = (42).__truediv__ (13)
# A = 42 // 13 #floor division
# a = (42).__floordiv__ (13)
# A = 42 % 13 #modulus
# a = (42).__mod__ (13)
# A = 42 ** 13 #exponentiation
# a = (42).__pow__ (13)
# A = 42 ** 0.5 #square root
# number = 42
# a = math.sqrt(number)
# A = 42 ** (1/3) #cube root
# print(a)
# print(A)
                    # Strings 
# name = 'Musa'
# print (name.upper())
# print(name)
# print(dir(name))

# p = """ Hi, welcome to my journey of ai understanding 
# and development. I have started with image processing 
# and computer vision, now i am starting python to shape 
# my learning process. """
# print (p)

# name = 'Musa'
# age = 22
# print (f'My name is {name} and I am {age} years old') 

# name = 'Musa'
# print(f"Name: {name:*^20}")

# x = -22/100
# print(f'{x:= 10.1%}')

# x = 22
# print (f'binary: {x:b}') #binary
# print (f'octal: {x:o}') #octal
# print (f'hexadecimal: {x:x}') #hexadecimal

#                     Help

# x = help(False)
# print(x)

# x = help()
# print(x)

                        # Conditionals

# grade = 98
# if grade >= 95:
#     print('A+')
# if grade >= 90:
#     print('A')
# elif grade >= 80:
#     print('B')
# elif grade >= 70:
#     print('C')
# elif grade >= 60:
#     print('D')
# else:
#     print('F')  

# language = input("Please enter your favorite programming language: ")
# if language == 'python':
#     print('Yes! You are a pythonist') 
# elif language == 'java':
#     print('Alright, you are a java developer.') 
# elif language == 'javascript':
#     print('You are a javascript developer.') 
# elif language == 'c++':
#     print('You are a c++ developer.') 
# elif language == 'c#':
#     print('You are a c# developer.') 
# elif language == 'php':
#     print('You are a php developer.') 
# elif language == 'ruby':
#     print('You are a ruby developer.')
# else:
#     print('You are a developer. just start!')

# x = True
# y = False
# z = 5 > 3
# print(z)

# x = 9
# y = 10
# if x < y:
#     print('x is less than y')
# else:
#     print('x is not less than y')

# x = 9
# y = 10
# z = 15 

# if x < y and y < z:
#     print('x is less than y and z')
# elif x < y or y < z:
#     print('x is less than y or z') 
# else:
#     print('x is not less than y and z')

# a = 3
# b = 1
# boolval = a > b
# if boolval:
#     print('a is greater than b')
# else:
#     print('a is not greater than b') 

# def are_you_sad ( is_rainy, has_umbrella ):
#     if is_rainy == True and has_umbrella == False:
#         print('You are sad')
#     else:
#         print('You are not sad') 

# are_you_sad(True, False)
# are_you_sad(True, True) 
# are_you_sad(False, True)
# are_you_sad(False, False)

def are_you_sad ( is_rainy, has_umbrella ):
    if is_rainy and not has_umbrella:
        print('You are sad') 
    else:
        print('You are not sad') 

are_you_sad(True, False)
are_you_sad(True, True)
are_you_sad(False, True)
are_you_sad(False, False)