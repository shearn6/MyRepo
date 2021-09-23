from random import shuffle as shuff
import os

os.system("cls" if os.name == "nt" else "clear")
# if os.name == "int"
   # os.system("cls")
# else:
   # os.sustem("clear")

# import random

my_list = ["Apple", "Banana", "Cherry", "Date", "Fig", "Guava"]
print(my_list)

#random.shuffle(my_list)
element = my_list.index("Guava")
print(element)
shuff(my_list)
print(my_list)
element = my_list.index("Guava")
print(element)
