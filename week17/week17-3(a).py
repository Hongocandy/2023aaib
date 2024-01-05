a=int(input())
ans=0
for i in range(1,2*a+2,2):
    ans+=i
print(f'f({a})={ans}',end='')
