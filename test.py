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
a=300 
print(sys.getrefcount(a))