uncle_sam = 1.08
pay_the_server = 1.15
food_stuff = float(input("How much was your meal? "))
corporate_cut = uncle_sam * food_stuff
pocket_book_pain = corporate_cut * pay_the_server
print("You need to leave " + str(pocket_book_pain) + " on the table to cover tax and tip.")
