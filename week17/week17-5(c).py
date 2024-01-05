a=list(map(int,input().split() ))
b=len(a)
for i in range(b):
    
    if a[i]==0:break
c=max(a)
d=min(a)       
print(f'[{d},{c}]',end='')