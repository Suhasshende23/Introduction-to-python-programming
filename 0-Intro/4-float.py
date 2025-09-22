#Float datatype storing decimel numbers
x= float(input("whats x? "))
y= float(input("whats y? "))

z=(x+y)
print(x)

# Round to nearest number
z=round(x+y)
print(z)

print(f"{z:,}") # commaa to given answer  i.e. 4,301


#devision
z=round(x/y,2) #20.04 round upto two decimal places
print(z)

#using f string to round upto two decimal places
print(f"{z:.2f}")
