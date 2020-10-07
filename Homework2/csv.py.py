info_dictn = {}
with open('input1.csv',newline='')as f:
    reader = csv.reader(f)
    for lineArray in reader:
        for key in lineArray:
            if key in info_dictn:
                info_dictn[key] = info_dictn[key]+1
            else:
                info_dictn[key] = 1

for key, count in info_dictn.items():
  print(key,count)