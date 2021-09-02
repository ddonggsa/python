#심사문제 18.6 p240
start,stop = map(int,input().split())
i = start

while True:
  if i % 10 ==3:
      i += 1
      continue
  if i > stop:
      break
  print(i,end=' ')
  i += 1

#심사문제 19.5 p250
a = int(input())

for i in range(1,a+1):
    for j in range(a+1-i):
            print(' ',end = ' ')
    for j in range(2*i-1):
            print('*',end = ' ')
    print( )
