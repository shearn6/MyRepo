#create a program that makes a list of the users favorite foods
#the list should be any size that the user wants
#print out the list for the user
#ff = favorite food

my_list = []
yes_list = ["y", "yes", "yea", "yeah", "ok", "k", "Yes", "Yeah", "Yes", "Y", "Yea", "K", "OK", "Ok"]
no_list = ["n", "no", "No", "NO", "Hell no", "nope", "Nope", "nah", "Nah", "Hell No", "N"]
while True:
    question = input("Would you like to add a food to your list? \ny|n: ").lower()
    if question in yes_list:
        my_list.append(input("What is one of your favorite foods? "))
    elif question == "n":
        break
    else:
        print("You did not select y or n")

for i in my_list:
    print(i + " is my favorite food!")
