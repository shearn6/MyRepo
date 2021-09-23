from random import shuffle as shuf
def mult(ans_list, quest, ans, points):
    abcd = ["A", "B", "C", "D"]
    # list1 = ["Blue", "Brown", "Green", "Purple"]
    shuf(ans_list)
    print(quest)
    for i, j in zip(abcd, ans_list):
        print(f"{i}. {j}")
    # print(" " + i + "." + j)
    while True:
        answer = input("Answer: ").upper()
        if answer in abcd:
            break
        else:
            print("Invalid response.")
    if abcd.index(answer) == ans_list.index(ans):
        points = points + 1
    return points

def main():
    score = 0
    score = mult(["Blue", "Brown", "Green", "Purple"], "What color is the sky on a nice day?", "Blue", score)
    score = mult(["Green", "Brown", "Pink", "Clear"], "What color is healthy grass?", "Green", score)
    score = mult(["This one", "Nope", "Not this", "Don't even try"], "Which is correct?", "This one", score)
    print(score)
    if score > 8:
        print("You get an A")
    elif score > 7:
        print("You get a B")
    elif score > 6:
        print("You get a C")
    elif score > 5:
        print("You get a D")
    else:
        print("You have failed.")
        main()

if __name__ == "__main__":
    main()




