#Anthony Laymond
#1636486
listofwords= list(input().split(" "))
consisword = []

for l in listofwords:
    consisword.append(listofwords.count(l))

for i in range(len(listofwords)):
    print(listofwords[i], consisword[i])
