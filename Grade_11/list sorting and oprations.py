n=['Jayaesh','Adarsh','Jai','Rethan', 'Sanjay', 'Nitin', 'Ddesignerpro13', 'Viswant']
print('Few Boys in Cs class' )
n.sort() #Sorts based in ASCII value of first alphabet
count=0
while count<=(len(n)-1):
    print(count,n[count])
    count+=1
print()
print('Max: ', max(n))#Checks for first letter
print('Min: ', min(n))#Checks for first letter
