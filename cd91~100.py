'''
#6091
a, b, c = map(int,input().split())

d = 1
while d%a!=0 or d%b!=0 or d%c!=0 :
  d += 1
print(d)

#6092
n = int(input())
a = input().split()

for i in range(n):  #n-1까지 a 순서대로 저장되어 있는 값 저장
    a[i] = int(a[i])

d = []  #d라는 리스트에 0 저장
for i in range(24): #0~23
    d.append(0)

for i in range(n):  #해당 자리수 카운트
    d[a[i]] += 1

for i in range(1,24):
    print(d[i], end=' ')

#6093
n = int(input())
a = list(map(int,input().split()))

for j in range(n-1,-1,-1):
    print(a[j], end=' ')

#6094
n = int(input())
a = list(map(int,input().split()))

print(min(a))

#6095
d = []
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)

n = int(input())
for i in range(n):
    a, b = map(int,input().split())
    d[int(a-1)][int(b-1)] = 1

for i in range(20):
    for j in range(20):
        print(d[i][j], end=' ')
    print("")

#6096
d = []  #d 리스트 선언
for i in range(19): #d 20개 추가하기 위한 반복
    d.append([])    # d 리스트 추가
    for j in range(19): #열길이 20개
        d[i].append(0)  #자리마다 0넣기

#h, w = map(int,input().split())
a = [[0]*w]*h

for i in range(19):
    d[i] = list(map(int, input().split()))

n = int(input())
for i in range(n):
    a, b = map(int,input().split())

    for j in range(19):
        if d[a-1][j] == 0:
            d[a-1][j] = 1
        else:
            d[a-1][j] = 0
        if d[j][b - 1] == 0:
            d[j][b - 1] = 1
        else:
            d[j][b - 1] = 0

for i in range(19):
    for j in range(19):
        print(d[i][j], end = ' ')
    print("")

'''
