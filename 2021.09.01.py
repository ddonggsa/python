#심사문제 9.4 p113
s = "\'Python\' is a \"programming language\"\nthat lets you work quickly\nand\nintegrate systems more effectively."
print(s)
#리스트(list)->대괄호로 묶어줌 ->[]
#튜플(tuple)->읽기전용 리스트(삭제,추가 불가능), 괄호로 묶어줌 ->()

#심사문제 10.5 p123
x = int(input())
a = tuple(range(-10,10,x))
print(a)

#심사문제 11.8 p157
x = list(input().split())
del x[-5::]
print(tuple(x))

#심사문제 11.9 p158
x = input()
y = input()
print(x[1::2]+y[0::2])

#심사문제 12.5 p168
x =input().split(' ')
y = input().split(' ')
lux = dict(zip(x,y))
print(lux)

#심사문제 13.7 p185
x=input()
y=input()

if y=='Cash3000':
    print(int(x)-3000)

if y=='Cash5000':
    print(int(x)-5000)

#심사문제 14.7 p195
a,b,c,d= map(int,input().split(' '))
if 0>a or 100<100 or 0>b or 100<b or 0>c or 100<c or 0>d or 100<d:
    print("잘못된 점수")
else:
    if ((a+b+c+d)/4)>=80:
        print("합격")
    else:
        print("불합격")

#심사문제 15.4 p202
age = int(input())
balance = 9000
if age>=19:
    print(balance-1250)
elif 13<=age<19:
    print(balance-1050)
else:
    print(balance-650)
    










