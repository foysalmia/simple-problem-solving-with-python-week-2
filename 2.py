def calculation(x, y):
    addition = x+y
    substraction = x-y
    return addition, substraction


result = calculation(15, 10)
print(type(result))
print(f"Addition = {result[0]}\nSubstraction = {result[1]}")
