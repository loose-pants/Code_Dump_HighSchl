rows = int(input("Enter number of rows: "))
cf = 1

for i in range(1, rows+1):
    for space in range(1, rows-i+1):
        print(" ",end="")
    for j in range(0, i):
        if j==0 or i==0:
            cf = 1
        else:
            cf *= (i - j)//j
        print(cf, end = " ")
    print()
