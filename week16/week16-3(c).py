a=input('')
if a.isupper():print('U',end='')
elif a.islower():print('L',end='')
elif a.isdecimal():print('D',end='')
else:
    print('O',end='')
