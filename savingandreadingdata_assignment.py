import datetime
date = datetime.date.today()
question = input("Have you previously used this program?\n Y|n: ").lower()

if question != "n":
    while True:
        try:
                with open("goodbad.txt","r") as f:
                    print(f.read())
                    break
        except FileNotFoundError:
            print("No previous activity shown.")
            break
elif question == "n":
    print("Welcome! :)")
else:
    print("Input Error")
    question = input("Have you previously used this program?\n Y|n: ").lower()

goodbad = input("How are you feeling today?\ngood or bad\n").lower()
while True:
    if goodbad == "good" or goodbad == "bad":
        file = open("goodbad.txt", "w")
        file.write(f"On {date} you had a {goodbad} day")
        break
    else:
        print("That wasn't good or bad")
        goodbad = input("How do you feel?\ngood or bad:\n").lower()
        continue
