rows = int(input("Enter number of rows: "))
k = 0
for i in range(1, rows+1):
    for j in range(1, (rows-i)+1):
        print(end="  ")
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
    k = 0
    print()
#j rep. Spaces
#k rep. Flag control
#====Lower triangle=====
for i in range(rows-1, 1, -1):
    for s in range(0, rows-i):
        print("  ", end="")
    for j in range(i, 2*i-1):
        print("* ", end="")
    for k in range(1, i-1):
        print("* ", end="")
    print()
#s rep. Space
#the formula 2*(i-1) is arbitary to reach goal
