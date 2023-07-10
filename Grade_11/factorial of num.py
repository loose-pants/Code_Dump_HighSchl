#print 1+1/1!+1/2!+1/3!
from math import factorial
x=int(input('enter no. '))
summ=1
for i in range(x):
    val= summ+(1/factorial(i+1))
print(val)
print(factorial(0))
