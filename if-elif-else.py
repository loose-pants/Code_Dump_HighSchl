m1= float(input('Enter mark '))
m2= float(input('Enter mark '))
m3= float(input('Enter mark '))
m4= float(input('Enter mark '))
m5= float(input('Enter mark '))
mark=((m1+m2+m3+m4+m5)/400)*100
if mark>90:
    grade='A1'
elif mark>80 and mark <=90:
    grade='A2'
elif mark>70 and mark<=80:
    grade='B1'
elif mark>60 and mark <=70:
    grade='B2'
elif mark>50 and mark<=60:
    grade='C1'
elif mark>40 and mark<=50:
    grade='C2'
elif mark>=33 and mark <=40:
    grade='D'
elif mark>20 and mark <33:
    grade='E1'
else:
    grade='E2'
    
print('Your grade is ',grade,'\n And % is',mark)