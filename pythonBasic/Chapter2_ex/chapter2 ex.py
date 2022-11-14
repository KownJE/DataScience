# 1번
su = 5 # 수량
dan = 800 # 단가

print('su 주소 : ' , id(su))
print('dan 주소 : ' , id(dan))

Totalgold = su * dan # 총금액은
print('금액 = ' , id(Totalgold))

#--------------------------------------

# 2번

# y = 2.5 * (x ** 2) + 3.3 * x + 6

x = 2
y = 2.5 * x**2 +3.3 * x +6
print('2차 방적식 결과 =' , y)

#---------------------------------------

# 3번

fat = 25
carbohydrate = 520
protein = 45
Total_Cal = (fat * 9) + (carbohydrate *4) + (protein *4)

print('지방의 그램을 입력하세요 : ' , fat)
print('탄수화물의 그램을 입력하세요 : ' , carbohydrate)
print('단백질의 그램을 입력하세요 : ' , protein)
print('총칼로리 : ' , Total_Cal , 'cal')

#------------------------------------------

# 4번

word1 = input('첫번째 단어 : ')
word2 = input('두번째 단어 : ')
word3 = input('세번째 단어 : ')
#abbr = word1[0] + word2[0] + word3[0]
#abbr = f'{word1[0]}{word2[0]}{word3[0]}'
abbr = f'{word1[0]}{word2[0]}{word3[0]}'

print("=" * 15)
print(f"약자: {abbr}")


#===========================================

# 연습문1

k = 80
e = 75
m = 90
s = 95
avg = (k + e + m + s) / 4

print("평균 : " , avg)

#-------------------------------------------

# 연습문2
num = 13
check = (num%2 ==1)
print(int(check))

num = 16
check = (num%2 == 1)
print(int(check))

#---------------------------------------------

# 연습문3,4

# 3
hong = "881120-1068234"
print(hong.index("-"))
print(hong[:6])
print(hong[7:])

# 4
print(hong.rfind("1"))
print(hong[7])

#--------------------------------------------

# 연습문제 5

str = "a:b:c:d"
print(str.replace(":","#"))

#---------------------------------------------

# 연습문제 6

str2 = ['우리','끝까지',"힘내요!"]
print(f''.join(str2))
print(f"\"{''.join(str2)}\"")
