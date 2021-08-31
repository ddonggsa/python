## map, split사용
a,b = map(int,input(" 두가지 숫자를 입력하세요: ").split(','))
print(a+b)
#map->매번 int로 하나하나바꿔줘야 하는 번거로움 없이 한번에 바꿔줌
#split->숫자 구분기호 무엇인지 알려주는 것 

##심사문제 파이썬 코딩도장 p82
a,b,c = map(int,input().split())
##심사문제 6.7 p83
a= 50
b = 100
c = None
print(a)
print(b)
print(c)
##심사문제 6.8 p83
a,b,c,d = map(int,input().split())
print((a+b+c+d)//4)
## sep 사용
print(1,2,3,sep =", ")
#->1, 2, 3
#sep-> print되는 숫자나 문자 구분지어 출력하게함

##심사문제 7.5 p90
year, month, day, hour, minute, second = input().split()

print(year,month,day,sep = "-",end='T')
print(hour,minute,second,sep=':')





