'''
a, b = input().split()
print(int(a) != int(b))

n = int(input())
print(bool(n))

a = bool(int(input()))
print(not a)

a, b = input().split()
print(bool(int(a)) and bool(int(b)))

a, b = input().split()
print(bool(int(a)) or bool(int(b)))

a,b = map(int,input().split())
print((bool(a) and not(bool(b))) or (not(bool(a)) and bool(b)))

a,b = map(int,input().split())
print((not bool(a) and not(bool(b))) or (bool(a) and bool(b)))

a,b = map(int,input().split())
print((not bool(a) and not(bool(b))))

a = int(input())
print(~a)

a, b = map(int,input().split())
print(a & b)
'''

