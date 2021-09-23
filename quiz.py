# make the following quiz
# asks 10 questions
# randomizes the potential answers
# calculates the numeric grade
# gives a letter grade

x = 0
score = x

from random import shuffle as shuff
import os

os.system("cls" if os.name == "nt" else "clear")

# Question 1
print("1. What color is the sky? ")
answer_1 = ["Blue", "House", "Table", "Book"]
shuff(answer_1)
print(answer_1)
house = input("Answer here: ")
if house == "Blue" or house == "blue":
    print("Correct")
    x = x + 1
else:
    print("Incorrect: Answer is Blue")

#Question 2
print("2. What is 1 + 1 = ?")
answer_2 = ["1", "2", "3", "-1"]
shuff(answer_2)
print(answer_2)
math_1 = input("Answer here: ")
if math_1 == "two" or math_1 == "2":
    print("Correct")
    x = x + 1
else:
    print("Incorrect: Answer is 2")

#Question 3
print("3. What is 17 * 10 = ?")
answer_3 = ["170", "210", "27", "70"]
shuff(answer_3)
print(answer_3)
math_2 = input("Answer here: ")
if math_2 == "170":
    print("Correct")
    x = x + 1
else:
    print("Incorrect: Answer is 170")

# Question 4
print("4. Who is the 1st president of the United States?")
answer_4 = ["George Washington", "Thomas Jefferson", "Donald Trump", "Bernie Sanders"]
shuff(answer_4)
print(answer_4)
pres_1 = input("Answer here: ")
if pres_1 == "George Washington" or pres_1 == "george washington" or pres_1 == "George washington" or pres_1 == "Washington" or pres_1 == "washington":
    print("Correct")
    x = x + 1
else:
    print("Incorrect: Answer is George Washington")

# Question 5
print("5. What type of animal is a tiger?")
answer_5 = ["Feline", "Canine", "Ursidae", "Insect"]
shuff(answer_5)
print(answer_5)
animal = input("Answer here: ")
if animal == "Feline" or animal == "feline":
    print("Correct")
    x = x + 1
else:
    print("Incorrect: Answer is Feline")

# Question 6
print("6. How many days are in a week?")
answer_6 = ["1", "7", "6", "10"]
shuff(answer_6)
print(answer_6)
week = input("Answer here: ")
if week == "7" or week == "seven":
    print("Correct")
    x = x + 1
else:
    print("Incorrect: Answer is 7 days")

# Question 7
print("7. How do you correctly spell the day after Tuesday?")
answer_7 = ["Wednesday", "Wendsday", "Wensday", "Wednedsday"]
shuff(answer_7)
print(answer_7)
wednesday = input("Answer here: ")
if wednesday == "wednesday" or math_1 == "Wednesday":
    print("Correct")
    x = x + 1
else:
    print("Incorrect: Answer is Wednesday")

# Question 8
print("8. How do you spell the element Al?")
answer_8 = ["Aluminum", "Alumnum", "Alumenum", "Alumeinum"]
shuff(answer_8)
print(answer_8)
aluminum = input("Answer here: ")
if aluminum == "Aluminum" or aluminum == "aluminum":
    print("Correct")
    x = x + 1
else:
    print("Incorrect: Answer is Aluminum")

# Question 9
print("9. Which planet is closest to the sun?")
answer_9 = ["Venus", "Mercury", "Saturn", "Mars"]
shuff(answer_9)
print(answer_9)
planet = input("Answer here: ")
if planet == "Mercury" or planet == "mercury":
    print("Correct")
    x = x + 1
else:
    print("Incorrect: Answer is Mercury")

# Question 10
print("10. Which chess piece can't move in a straight line?")
answer_10 = ["Knight", "Pawn", "Bishop", "Rook"]
shuff(answer_10)
print(answer_10)
chess = input("Answer here: ")
if chess == "Knight" or chess == "knight":
    print("Correct")
    x = x + 1
else:
    print("Incorrect: Answer is Knight")

# Total Score
score = float(x / 10) * 100
print(x,"out of 10, that is",score, "%")
if score >= 90:
    print ("You have received an A")
elif score >= 89 and score <= 80:
    print ("You have received a B")
elif score >= 79 and score <= 70:
    print ("You have received a C")
elif score >= 69 and score <= 60:
    print ("You have received a D")
elif score <= 59:
    print ("You have received an F")




