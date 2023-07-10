#Stack implementation
def putin(lis,item):
    global top
    if len(lis)>lis_limit:
        return "Overflow"
    else:
        lis.append(item)
        top=lis[0]
def throwout(lis):
    if len(lis)==0:
        return "Underflow"
    else:
        lis.pop()
        return "^ Item removed"

def peekaboo(lis):
    if len(lis)==0:
        return "Underflow"
    else:
        print("items in stack are as follows")
        for items in lis:
            print(items, end=' ')
        return True,'\n'
pom=[]
lis_limit=8 #flexiable
top=None
while True:
    print('''Choose your option
      1.Insert 
      2.Pop 
      3.See list
      4.EXIT''')
    do=int(input('enter your choise : '))
    if do==1:
        a=str(input('enter item '))
        putin(pom, a)
    elif do==2:
        throwout(pom)
    elif do==3:
        peekaboo(pom)
    else:
        print('bye!')
        break



