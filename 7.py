sample_dict = {'a': 100, 'b': 200, 'c': 300}
isPresent = False
value = 100

for x in sample_dict:
    if sample_dict[x] == value:
        isPresent = True
        break

if isPresent:
    print("Present")
else:
    print("Not Present")
