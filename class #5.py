def is_num():
    while True:
        try:
            num = int(input("Give me a number: "))
            break
        except ValueError:
            print("This is not a number")
            continue
    return num

my_list = []
x = is_num()
y = is_num()
z = is_num()
print(x, y, z)
my_list = []
my_list.append(is_num())
my_list.append(is_num())
my_list.append(is_num())
my_list.append(4)
my_list.append(5)
my_list.append(6)
my_list.append(7)
my_list.append("Apple")
my_list.append("Potato")

length  = len(my_list)
count = 0
while count < length:
    print(my_list[count])
    count +=1
print(length[-1])
print(my_list)

#length = len(my_list)
#count = 0
#while count < length:
#   print(my_list[count])
#   count +=1

for i in my_list:
        print(i)

#for life

