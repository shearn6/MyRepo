import os
day = input("How was your day? (good or bad)")
response = day
while True:
    print(day)
    while response != "good" or "bad":
        print("You did not enter a valid response. Please try again")
    continue
    if response == "good" or response == "bad":
            with open ('shadow.txt', 'r') as fShadow

filePath = os.path.join(os.path.expanduser('~'), 'Desktop', 'result.txt')

with open(filePath, 'w') as file:
    file.write(f"{day})