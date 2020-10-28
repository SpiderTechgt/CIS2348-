number = input().split()
result = []

for num in number:
    num = int(num)
    if num >= 0:
        result.append(num)

result.sort()
for num in result:
    print(num, end=' ')