sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
values = []
for x in sample_dict:
    if x in keys:
        values.append(sample_dict[x])

result = dict(zip(keys, values))
print(result)
