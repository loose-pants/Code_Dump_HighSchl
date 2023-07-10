for i in range(5):
    for j in range(5):
        if i==j or i>j:
         print('*',end='')
         i-=1
        else:
            print('')
