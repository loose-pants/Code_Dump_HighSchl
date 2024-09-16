print("holla My dear friend Paarth u Vakhriya")
#from your dear friend 

for i in range(6):
    for j in range(6):
        if i==j and i>j or i<j :
         print('+',end=' ')
        else:
             print('',end=' ')
    print(' ')

for i in range(6):
    for j in range(6):
        print('*',end=' ')
    print()
print()

for i in range(4):
    print('',end='o')
    for j in range(6):
        print('|',end='x')
    print()
