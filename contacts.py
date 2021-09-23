#make a python program that takes in a person's name, number, email and save it to a file named
# contacts.txt. Have the file be able to take in more than one name at a time
def main()
    q = "y"
    while q != "n":
        name = input("Enter the name to add: ")
        phone = input("Enter phone number here: ")
        email = input("Enter email here: ")

        with open("contacts.txt","a") as contacts:
            contacts.write(f"{name}, {phone}, {email}\n")
        while True:
            q = input("Would you like to add another contact? Y|n: ").lower()
            if q == "n" or q == "y" or q == "":
                break
            else:
                print("You did not enter a correct choice.")

if __name__ == "__main__":
    main()


# with open ("contacts.txt","w") as contacts:
    # contacts.write("Enter name here: \n")
    # contacts.write("Enter email here: \n")
    # contacts.write("Enter cell phone number here: \n")


# CSV- comma separated value

# file.write(name + \n)

