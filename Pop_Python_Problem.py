from is_num import is_num
name = []
price = []


while True:
    name.append(input("What is your name: \n"))
    print(is_num("How much did your meal cost? \n"))
    while True:
        q = input("Add another? y|n: ").lower()
        if q == "y" or q == "n":
            break
        else:
            print("Please type 'y' or 'n' to continue with the program: ")
for i, j in zip(name, price):
    print(f"{i} ordered food.")