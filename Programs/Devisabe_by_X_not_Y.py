arr = list(range(100, 500, 2))

newArr = []

for i in arr:
    if (i % 7 == 0) and (i % 5 != 5):
        newArr.append(i)
        
print(newArr)