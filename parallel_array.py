from is_num import is_num


name = []
age = []
q = "y"


while q == "y" or q == "":
    name.append(input("What is your friend's name: \n"))
    age.append(is_num("How old are they? \n"))
    while True:
        q = input("Add another? Y|n: ").lower()
        if q == "y" or q == "" or q == "n":
            break
        else:
            print("Please use a 'y' or a 'n'.")
for i, j in zip(name, age):
    print(f"You have a friend named {i} and they are {j}.")
