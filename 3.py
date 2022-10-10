list1 = ["M", "na", "i", "Bo"]
list2 = ["y", "me", "s", "nd"]

result = []

for x in range(len(list1)):
    tmp = list1[x]+list2[x]
    result.append(tmp)

print(result)
