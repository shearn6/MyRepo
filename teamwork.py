# we chose to go with Williams solution since it was simplest
people_cost = input('''Please type a name and their cost of food. You may do this for as many people as you like EX: Jane 19.42 Jack 23.40 ''')
people = people_cost.split()
cost = []

for i in people:
    try:
        if isinstance(int(i), int) or isinstance(int(i), float):
            people.remove(i)
            cost.append(int(i))
    except (TypeError, ValueError) as error:
        continue

total = sum(cost)
average = int(total)/(len(people))
print(cost, people, total, average)
