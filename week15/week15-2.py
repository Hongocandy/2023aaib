                                                                                                        #現在要試著模擬看看，方法1
s='00111'
N=len(s)
zero=0 #等一下也要
one = 0 #想找出全部的1
for i in range(N):
   if s[i]=='1':one +=1
#現在就知道總共有幾個one

print('一開始的時候，都在右邊，統計結果','Zero',zero,'one',one)
ans=0
for i in range(N-1):#要逐個去修正
   if s[i]=='0': #吐出0給左邊
    zero += 1 #左邊多一個0
   if s[i]=='1': #兔出'1'，給左邊
    one -= 1 #右邊少一個1
   print('中間過程中','zero',zero,'one',one)
   ans=max(ans,zero+one)#最好的答案，最大的值
print('答案找出來了',ans)