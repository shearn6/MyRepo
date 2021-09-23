#num = int(input("Give me a number"))
#print(num)

while True:
    try:
        num = int(input("Give me a number: "))
    except:
        print("You did not enter a number ")
        continue
print(num)

