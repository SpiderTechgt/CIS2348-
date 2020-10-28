#Anthony Laymond
#1636486
vary = input().split()
result = []

for var in vary:
    var = int(var)
    if var >= 0:
        result.append(var)

result.sort()
for var in result:
    print(var, end=' ')
