list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

list2 = list(reversed(list2))

x = tuple(zip(list1, list2))
for y in x:
    print(f"{y[0]} {y[1]}")
