key='panda'
correct = False
while not correct:
    inp=input('Enter secret key: ')
    if inp == key:
        print('Correct')
    else:
        print('Wrong')