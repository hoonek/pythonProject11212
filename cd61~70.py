'''
a, b = map(int,input().split())
print(a & b)

a, b = map(int,input().split())
print(a | b)

a, b = map(int,input().split())
print(a ^ b)

a, b = input().split()
a = int(a)  #변수 a에 저장되어있는 값을 정수로 바꾸어 다시 변수 a에 저장
b = int(b)
c = (a if (a>=b) else b)
print(int(c))

a, b, c = map(int, input().split())
print(min(a,b,c))

a, b, c = map(int, input().split())
if a % 2 == 0:
    print(a)
if b % 2 == 0:
    print(b)
if c % 2 == 0:
    print(c)

    a, b, c = map(int, input().split())
if a % 2 == 0:
    print('even')
else:
    print('odd')
if b % 2 == 0:
    print('even')
else:
    print('odd')
if c % 2 == 0:
    print('even')
else:
    print('odd')


a = int(input())
if a<0:
    if a%2==0:
        print('A')
    else : print('B')
else:
    if a%2==0:
        print('C')
    else : print('D')

    a = int(input())
if 90 <= a:
    print('A')
if 70 <= a and 90 > a:
        print('B')
if 40 <= a and 70 > a:
        print('C')
if 0 <= a and 40 >a:
        print('D')

a = input()
if a == 'A':
    print('best!!!')
elif a == 'B':
    print('GOOD!!')
elif a == 'C':
    print('run!')
elif a == 'D':
    print('slowly')
else:
    print('what?')

'''



a = int(input())
if a //3 == 1 :
    print('spring')
elif a // 3 == 2:
    print('summer')
elif a // 3 == 3:
    print('fall')
else:
    print('winter')

