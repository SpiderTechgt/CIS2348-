name = input()
other = name.replace('','')
low = 0
high = len(other)-1
bagg = False
while low<high:
    if (other[low]!=other[high]):
        bagg= True
        break
    low+=1
    high-=1
if bagg:
    print(name,"is not a palindrome")
else:
    print(name,"is a palindrome")