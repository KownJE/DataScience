# 4번 문제
s = int(input('number : '))
for i in range(1, s + 1) :
    print("*"*i)

#------
# 5번 문제
s2 = int(input('number2 : '))
for i2 in range(1, s2 +1):
    print(" "*(s2-i2)+"*"*i2)

# ======== 그 외
n = int(input())

for i in range(n,0,-1):
    print("*"*i)

#---
n = int(input())

for i in range(n, 0, -1):
   print(" "*(n-i)+"*"*(i))
