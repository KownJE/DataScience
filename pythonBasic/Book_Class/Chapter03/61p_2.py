score = int(input('점수 입력:'))
if score >= 85 and score <= 100 :
    print('우수')
else:
    if score >= 70:   # 중첩된 if는 그리 좋지 않다.
        print('보통')
    else:
        print('저조')
