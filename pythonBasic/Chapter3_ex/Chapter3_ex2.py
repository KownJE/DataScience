# 2번
import random

print('>>숫자 맞추기 게임<<')
com = random.randint(1, 10) # 1~ 10 사이 난수 발생

while True:
    my = int(input('예상 숫자를 입력하시오 :'))
    if my == com :
        print('~~성공~~')
        break
    elif my > com :
        print('더 작은 수를 찍어봐')
    elif my < com :
        print('더 큰 수를 찍어봐')

