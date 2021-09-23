# I worked with Sam cuz I'm stupid
import random

ran = random.randint(1,100)
count = 0

while count <= 4:
    guess = int(input("Tell me a number: "))
    count += 1
    if ran < guess:
        print("Your number is too high")
    elif ran > guess:
        print("Your number is too low")
    elif ran == guess:
        print("You guess correct!\nEnd Program")
        break
    if count == 5:
        print("You have used all your chances! Maybe next time...")
        print("The answer was " + str(ran))
        break
    if guess == 69:
        print("Ha ha ha ha ha ha ha ha")
