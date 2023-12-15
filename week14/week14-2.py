#大標題
##小標題 
1. 第一步
2. 第二步
  - 沒有數字的1
  - 沒有數字的2
  - 可以寫**程式碼**'print('Hello')'，要用數字123左邊的反撇
  
  #但是我們可以慢慢理解set()到底怎麼用
s={1,2,3,4,} #第一種用{}括號
print(s)
s=set( (1,3,5,7) ) #第二種set()裡面放你一開始要加入的東西，可用[圓括號] tuble

print(s)
s=set( [1,2,4,3] ) #第二種set()裡面也可以放{方括號}list的陣列的東西
print(s)
s=set('Hello') #第二種的set()裡面也可以放字串，會把他一個一個拆開
print(s)

#下面試試 .add()和.remove()

s.add(100)
print(s)
s.remove('H')
print(s)