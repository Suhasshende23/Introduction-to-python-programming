while True:
    n=int(input("Enter the number "))
    if n>0:
        break

for _ in range(n):
    print("meow")


def main():
    meow(3)

def meow(n):
    for _ in range(n):
        print("meow2")

main()



def main():
    number=get_number()
    meow(number)

def meow(n):
    for _ in range(n):
        print("meow3")

def get_number():
    while True:
        n=int(input("Enter the number :"))
        if n>0:
            return n

main()