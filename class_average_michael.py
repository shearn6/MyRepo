import os

def get_key(arg, dic):
    for key, value in dic.items():
        if value == arg:
            return key
def get_grade(name):
    while True:
        x = input(f"What is {name}'s grade: ").upper()
        if x in ('A', 'B', 'C', 'D', 'F'):
            return x
        else:
            print("Please give a letter grade (A,B,C,D,F) ")
def main():
    letter_grades = {'A':4, 'B':3, 'C':2, 'D':1, 'F':0}
    students = []
    grades = []
    again = "y"
    total = 0

    while again != "n":
        os.system("cls" if os.name == "nt" else "clear")
        students.append(input("What is the student's name?\n"))
        grades.append(get_grade(students[-1]))
        while True:
            again = input("Do you want to add another student? Y|n ").lower()
            if again in ("y", "", "n"):
                break
            else:
                print("Please use a 'y' or 'n'.")

    for grade in grades:
        total = total + letter_grades[grade]
    gpa = int(round(total / len(grades),0))
    gpa2 = round(total / len(grades),1)
    os.system("cls" if os.name == "nt" else "clear")
    for student, grade in zip(students, grades):
        print(f"{student}: {grade}")
    avg = get_key(gpa, letter_grades)
    print(f"The class average is {gpa2} which is roughly a {avg}")
if __name__ == "__main__":
    main()

