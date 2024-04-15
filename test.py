import math
from unittest import result
import numpy as np 
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

# def is_c_greater_than_d_plus_e (c, d, e): 
#     if c > d + e:
#         print (True)
#     elif c == d + e:
#         print ('Equal')
#     else:
#         print (False) 
# def is_c_greater_than_d_plus_e (c, d, e): 
#     if c > d + e:
#         print (True)
#     elif c == d + e:
#         print ('Equal')
#     else:
#         print (False) 
# is_c_greater_than_d_plus_e (1, 2, 3) 
# is_c_greater_than_d_plus_e (5, 2, 1) 
# is_c_greater_than_d_plus_e (3, 2, 1) 
# is_c_greater_than_d_plus_e (7, 6.9, 0.2)
# is_c_greater_than_d_plus_e (1, 2, 3) 
# is_c_greater_than_d_plus_e (5, 2, 1) 
# is_c_greater_than_d_plus_e (3, 2, 1) 
# is_c_greater_than_d_plus_e (7, 6.9, 0.2)
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

# def are_you_sad ( is_rainy, has_umbrella ):
#     if is_rainy and not has_umbrella:
#         print('You are sad') 
#     else:
#         print('You are not sad') 

# are_you_sad(True, False)
# are_you_sad(True, True)
# are_you_sad(False, True)
# are_you_sad(False, False)

# def are_you_sad ( is_rainy, has_umbrella ): 
#     return is_rainy and not has_umbrella

# print(are_you_sad(True, False))
# print(are_you_sad(True, True)) 
# print(are_you_sad(False, True))
# print(are_you_sad(False, False))

# def is_c_greater_than_d_plus_e (c, d, e): 
#     if c > d + e:
#         print (True)
#     elif c == d + e:
#         print ('Equal')
#     else:
#         print (False) 
# is_c_greater_than_d_plus_e (1, 2, 3) 
# is_c_greater_than_d_plus_e (5, 2, 1) 
# is_c_greater_than_d_plus_e (3, 2, 1) 
# is_c_greater_than_d_plus_e (7, 6.9, 0.2)
    #   Coming later
# def is_c_greater_than_d_plus_e (c, d, e): 
#     if c > d + e:
#         print ('C is greater than D plus E')
#     elif c == d + e:
#         print ('C equals D plus E')
#     else:
#         print ('C is less than D plus E') 

# is_c_greater_than_d_plus_e (c = input('Enter c: '), 
# d = input('Enter d: '), 
# e = input('Enter e: ') )  

                    # Iteration

# for number in [0,1,2,3,4,5,6]:
#     print(number)

# for number in range(0, 7):
#     print(number)

# x = list(range(6))
# print(x)

# a = list(range(0,8))
# print(a)

# fruits = ["Kiwi", "Mango", "Avocado"]
# for index, value in enumerate(fruits, start=1):
#     print(index, value)

# fruits = ["Kiwi", "Mango", "Avocado"]
# for index, value in enumerate(fruits, start=1):
#     if value == 'Mango':
#         break
#     print(index, value) 

# fruits = ["Kiwi", "Mango", "Avocado"] 
# for index, value in enumerate(fruits, start=1):
#     if value == 'Mango':
#         continue
#     print(index, value) 

# my_dic = {"Name": "Musa", "Credit": 9.99}
# for key in my_dic:
#     print(key) 

# for key, value in my_dic.items():
#     print(key, value)
                #Files
# with open('test.txt', 'r') as f:
#     contents = f.read()
# print(contents)

# with open('test.txt', 'w') as file:
#     file.write('I am learning files in python.\n')
#     file.write('I am understanding this now.\n') 
#     file.write('This is a grinning emoji\N{GRINNING FACE}')
# print('We have written to the file successfully!')  
                    #List
# list = ['Laptop', 'Book', 'Pen', 'Phone']
# print(list)
# list.append('Nuts')
# print(list)
# list[1]='Pencil'
# print(list)
                    #Slicing
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(numbers[0:3])
# print(numbers[:4])
# print(numbers[5:])

# text = 'Hello Guys'
# print(text[2:8])
# print(text[:5])
# print(text[0:])

# range_num = range(10)
# print(range_num[2:9]) 
# print(range_num[3:])
# print(range_num[:8])
# print(list(range_num[1:8]))
                        #Comprehensions
# numbers = [1, 2, 3, 4, 5]
# squares = [x**2 for x in numbers]
# print(squares)

# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = [x for x in numbers if x % 2 == 0]
# print(even_numbers)

# text = 'Hello Guys'
# uppercase_text = [letter.upper() for letter in text]
# print(uppercase_text) 
                        # Dictionary
# my_dict = {'Name':'Musa', 'Age':23, 'City':'Monrovia'}
# print(my_dict)
# print (my_dict['Name'])
# print (my_dict['Age'])
# print (my_dict['City']) 

# my_dict['Country'] = 'Liberia'
# print(my_dict) 

# my_dict['Age'] = 24
# print(my_dict) 

# del my_dict['City']
# print(my_dict)

# for key, value in my_dict.items():
#     print(key, value)

# print ('food' in my_dict)

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# new_dict = {v: k for k, v in my_dict.items()}
# print(new_dict)
                    # Functions and Lambda
# def add(a, b):
#     return a + b
# print(add(1, 2))

# def add(a, b): return a + b
# print(add(1, 2))

# my_list = [(1,'a'), (2,'b'), (3,'c')]
# sorted_list = sorted(my_list, key=lambda x: x[1])
# print(sorted_list)

# def roots(x):
#     return x**0.5

# print(roots(16))
                    # Classes
# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed 

#     def bark(self):
#         print("Woof Woof!") 

#     def __str__(self): 
#         return f"{self.name} is a {self.breed} dog." 

# my_dog = Dog("Fido", "A golden retriever")
# print(my_dog.name) 
# print(my_dog.breed) 
# my_dog.bark()

# print(my_dog)
                        # Exceptions
# try:
#     x = 1 / 0
#     print(x)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

# try:
#     with open("file.txt") as file:
#         content = file.read()
#         print(content) 
# except FileNotFoundError:
#     print("That file was not found.")

# def divide(a, b):
#     if b == 0:
#         raise ZeroDivisionError("You can't divide by zero!")
#     return a / b 

# try:
#     result == divide(10, 0)
# except ValueError as error:
#     print(error)

# except ZeroDivisionError as error:
#     print(error)

# else:
#     print(result)

# finally:
#     print("This code always runs.")
                    # Intro to numpy
digits = np.array(range(10))
print(digits)
print(digits.dtype)
print(digits.shape)
print(digits + 10)

slow_digits = list(range(10))
print(slow_digits)

nums = np.arange(100).reshape(20, 5) 
print(nums)