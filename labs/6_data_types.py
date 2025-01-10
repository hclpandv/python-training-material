num = 5
my_string = "Hello World" #string
my_float = 20.5	#float	
my_list = ["apple", "banana", "cherry"]	#list	
my_tuple = ("apple", "banana", "cherry")	#tuple	
my_range = range(6)	#range	

my_dict = { #dict
    "name" : "John", 
    "age" : 36
}		

my_set = {"apple", "banana", "cherry", "banana"}	#set	
my_bool = True	#bool	
my_bytes = b"Hello"	#bytes	
my_barray = bytearray(5)	#bytearray	
my_mem = memoryview(bytes(5))	#memoryview	
my_none = None

print(type(num))
print(type(my_float))
print(type(my_tuple))
print(type(my_set))
print(type(my_none))

print(my_set)
print(my_dict["name"])