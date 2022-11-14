# 홀짝 게임
import random

print("=" * 40)
print(">>홀짝 게임<<")
print("=" * 40)

continue_game = "yes"

while continue_game == "yes" :
    com = random.randint(0,1)
    select = int(input("홀/짝 당신의 선택은? [홀:0, 짝:1]"))

    if com == select :
        print("성공!")
    else :
        print("실패..")

        continue_game = input("게임을 계속 진행하시겠습니까? [yes or no]").lower()
else :
    print("게임을 종료합니다")