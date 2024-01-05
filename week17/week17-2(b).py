a=int(input())
b=a//3600
c=(a-(3600*b))//60
d=a%60
print('{:0>2}:{:0>2}:{:0>2}'.format(b,c,d),end='')