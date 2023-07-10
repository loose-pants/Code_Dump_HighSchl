import csv
import os
from pickle import dump,load
os.chdir('G:\\1Platinum\\Computer practicles')
print(os.getcwd())
#=============================================
with open('game.dat','wb') as binf:
    head=['aaa','aaaaa','bbb']
    dump(head,binf)
    arr=[['1','2','3'],['4','5','6'],[7,8,9]]
    for i in range(len(arr)):
        dump(arr[i],binf)
print('Done','Wrote-binary')

with open('game.dat','rb') as binf:
    head=load(binf)
    everything=[head]
    try:
        while True:
            head=load(binf)
            everything.append(head)
    except:
        for i in everything:
            print(i)
print('Read Binary######')
#=============================================
#=============================================

with open('game.csv','w',newline='') as csvf:
    pen=csv.writer(csvf,delimiter=',')
    pen.writerows(everything)
print('Wrote CSV###############')
with open('game.csv','r',newline='') as csvf:
    lens=csv.reader(csvf)
    for i in lens:
        print(i)
print('Read csv##################')
#=============================================