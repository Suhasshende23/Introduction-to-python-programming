'''
while True:
    try:
        x = int(input("Enter a number: ")) 
    except ValueError:
        # for handling errors
        print("Invalid input! Please enter a number.")
    else:
        print(f"Number is: {x}")
        break   
'''


'''
def main():
    x= get_num()
    print(f"number is {x}")


def get_num():
    while True:
        try:
            x = int(input("Enter a number: ")) 
        except ValueError:
            # for handling errors
            print("x is not number")
        else:
            
            break   
    return x

main()

'''

def main():
    x= get_num()
    print(f"number is {x}")


def get_num():
    while True:
        try:
            x = int(input("Enter a number: ")) 
        except ValueError:
             pass
        else:
            
            return x   
    

main()
