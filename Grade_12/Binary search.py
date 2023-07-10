#Bubble sort
from random import shuffle
l=list(range(0,100,5))
shuffle(l)
print(l)
for i in range(len(l)):
    for j in range(len(l)-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)
#binary search 
li=list(range(0,100,5))
def binsrc(l,x,high,low):
    while low<=high:
        mid=(low+high)//2
        if l[mid]==x:
            return mid
        if l[mid]>x:
            high=mid-1
            binsrc(l,x,low=low,high=high)
        elif l[mid]<x:
            low=mid+1
            binsrc(l,x,low=low,high=high)
    else:
        return -1

num=99
lo=0
hig=len(l)-1
print(binsrc(li,num,hig,lo))