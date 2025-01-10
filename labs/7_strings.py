#------ Quotes, \n, \t

string_1 = "Twinkle, Twinkle\nLittle\n" # use \n for line-break
string_2 = '\tStar\nHow'  # single quote works too
raw_string = r"I wonder\nwhat you are?"  # Notice r i.e. raw
print(string_1, string_2, raw_string)

string_block = '''Hello Friends,
I,Vikas Pandey, Welcome you to this Python Class.
I hope you are enjoying this session.
wish you all the best!!'''  # Triple Double quotes can also be used. try

print(string_block)

#----- String Functions

my_string = "https://vikiscripts.github.io/pythontutorial"

#slicing
print(my_string[0]) #Try Changing the numbers
print(my_string[0:-2]) # Try changing numbers and + and - too

print(len(my_string)) 
print(my_string + my_string) # Concatination
print(my_string * 2) # Repeatition

#spliting
print(my_string.split("/"))
print(my_string.split("."))
