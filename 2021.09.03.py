#심사문제 20.8 p259
a,b =map(int,input().split())

for i in range(a,b+1):
    if i % 35 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Fizz')
    elif i % 7 == 0:
        print('Buzz')
    else:
      print(i)

##list에 요소 추가 append
##list에 list연결해 확장 extend
##list에 특정 인덱스 요소 추가 insert
##list에서 마지막 요소 또는 특정인덱스의 요소삭제 pop,del
##list에서 특정값을 찾아서 삭제 remove
##list에서 특정값의 인데스 구하기 index
##list에서 리스트의 순서 뒤집기 reverse()
##lsit에서 리스트 요소 정렬하기 sort()
##list에서 모든 요소 삭제하기 clear()

