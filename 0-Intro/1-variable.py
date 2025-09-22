#Variables and Functions

#name is varable
# Ask user for their name
name=input("Whats your name ? ")

'''
#Say hello to user
print("hello")
print(name) #Print the value 
'''
'''
#Say hello to user
print("hello,"+ name) # Concat the value to hello
'''
'''
#Built in functions

https://docs.python.org/3/library/functions.html
'''

'''
#Say hello to user
print("hello", end=" ") # end print the value next to hello with " "space between them ,don't go to next line ,default argument is \n
print(name) #Print the value 
'''

'''
#Say hello to user
print("hello", end="??") # end print the value next to hello with "??" between them ,don't go to next line ,default argument is \n
print(name) #Print the value 
'''

'''
#Say hello to user
print("hello",name, sep="@@",end="") # its sep between values seperated by comma ,default is " " or you can customise it
print(name) #Print the value 
'''
'''
#print the quotes in the string 
#Say hello to user
print("hello \"friends\"") 
#hello "friends"
'''

#format string
#Say hello to user
print(f"hello {name}") # format string to print the dynamic name in the string
#hello "friends"
