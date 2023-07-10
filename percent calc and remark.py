m1= float(input('1.Enter English mark '))
m2= float(input('2.Enter Hindi mark '))
m3= float(input('3.Enter Tamil mark '))
ap= ((m1+m2+m3)/3)
if ap>=80:
    print(ap,'% Level 4, above agency-normalized standards')
elif ap>=70 and ap<=80:
    print(ap, '% Leve3, at agency-normalized standards')
elif ap>=60 and ap<=70:
    print(ap, '% Level 2, below, but agency-normalized standards')
elif ap>=50 and ap<60:
    print(ap, '%, Level 1, Well below agency-normalized standards')
elif ap>=40 and ap<50:
    print(ap,'% Level 1, too below agency-normalized standards')
elif ap<=39:
    print(ap, 'Remedial standards')
else:
    print(ap,'Better luck next time')
                        #End of code 