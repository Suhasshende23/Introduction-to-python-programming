# Ask user for their name
name=input("Whats your name ? ")

'''
#format string
#Say hello to user
print(f"hello {name}") # format string to print the dynamic name in the string
#hello "friends"
'''
'''
#remove the whtespaces from str
name=name.strip()
print(f"hello, {name}")


#Capitalises user name
name = name.capitalize()
print(f"hello, {name}")
'''

'''
#combine the both results 
name=name.strip().capitalize()
print(name)
'''

'''
#Title makes the each word first letter capital
name=name.strip().title()
print(name)
'''
'''
#split into many parts
first,last=name.split(" ")
print(f"hello {first}")
'''