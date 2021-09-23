
def amos():
    while True:
        try:
            return float(input("Enter number here:\n"))
        except ValueError:
            print("You did not enter a valid number.")



while True:
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    choice = input("Enter choice(1/2/3/4):\n ")
    if choice in ('1', '2', '3', '4'):
        num1 = amos()
        num2 = amos()
    if choice == '1':
        print(num1, " + ", num2, " = ", str(num1 + num2))

    elif choice == '2':
        print(num1, "-", num2, "=", str(num1 - num2))

    elif choice == '3':
        print(num1, "*", num2, "=", str(num1 * num2))

    elif choice == '4':
        print(num1, "/", num2, "=", str(num1 / num2))

    while True:
        q = input("Would you like to do another equation? Y|n: ").lower()
        if q not in ["n", "y"]:
            continue
        else:
            break
    if q == "n":
        break
    if q == "y":
        continue
    else:
        print("You did not select 'y' or 'n'. ")




