name = input("Enter your name: ")
# if the name match it will print the given statement
match name:
    case "Suhas":
        print("Welcome Suhas")
    case "Rutuja":
        print("Welcome Rutuja")
    case "Kewal":
        print("Welcome Kewal")
    case "Chirag":
        print("Welcome Chirag")
    case _:
        print("Welcome Stranger")
