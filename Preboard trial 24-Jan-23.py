#Bubble sort
sample_list=[40, 37, 33, 10, 34, 43, 47, 18, 24, 13, 35, 45, 29, 41, 32, 6, 12, 16, 30, 14, 23, 19, 39, 27, 28, 26, 7, 11, 49, 4, 8, 44, 5, 15, 25, 1, 2, 48, 36, 3, 20, 38, 17, 9, 42, 22, 21, 31, 46, 0]

print(sample_list)

def bubbly(l):                   #traditional version
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l
q=bubbly(sample_list)
print(q)

'''-----------------------------------------------------------'''

def bubbly2(l):                  #improved version
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[1+1],l[i]
    return l
p=bubbly2(sample_list)
print(p)
