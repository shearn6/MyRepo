# when you first start you have to enter A as the first grade or it'll keep saying you entered an incorrect grade,
# then you can enter whatever grade you choose. Can you tell me why that is?
# but it'll still print the incorrect grade entries...
name = []
grade = []
letter_grade = ["A", "B", "C", "D", "F"]
q = "y"
#score = x
#x = 0
grades = {"A":4.0, "B":3.0, "C":2.0, "D":1.0, "F":0.0}

def get_key(arg, dictionary):
    for key, value in dictionary.items():
        if value == arg:
            return key

while q != "n":
    name.append(input("What is the student's name? (Last, First) \n"))
    grade.append(input("What is their grade in the class by letter: \n").upper())
    while True:
        q = input("Would you like to add another student to the grade book? Y|n \n").lower()
        if q in ["n", "y", ""]:
            break
        else:
            print("Invalid Input")
for i, j in zip(name, grade):
        print(f"{i} has a(n) {j} in this class.")

count = {}
for i in grade:
    count [i] = count.get(i, 0) + 1
print(count)

# Grade calculations
# score = float(x/)
# print()


#