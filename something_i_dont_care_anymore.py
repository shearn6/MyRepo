def get_cost():
    while True:
        try:
            num = float(input("How much was their meal: "))
            break
        except ValueError:
            print("You did not give a number.")
            continue
    return num

if __name__ == "__main__":
    name = []
    food = []
    another = "y"
    while another != "n":
        name.append(input("What is the name of the person getting food?\n"))
        food.append(get_cost())
        while True:
            another = input("Would you like to add another person? \nY|n: ").lower()
            if another == "y" or another == "" or another == "n":
                break
            else:
                print("Please use a 'y' or an 'n' to continue: ")

    people = len(name)
    total = sum(food)
    average = total / people

    for i, j in zip(name, food):
        diff = average - j
        if diff > 0:
            print(f"{i} is paying ${diff:.2f} above the average price ${average:.2f}")
        elif diff < 0:
            diff = abs(diff)
            print(f"{i} is paying ${diff:.2f} below the average price ${average:.2f}")
