y=int(input('Enter Year '))
if y%100==0:
    if y%400==0:
        print('This is a leap year')
    else:
        print('No, its not a leap year')
elif y%4==0:
    print('Yes, this is a leap year')
else:
    print('No, this is a normal year')
