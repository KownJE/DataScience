num = 9
result = 0

# 무조건 이렇게 하세용
if num >= 5:
    result = num * 2
else:
    result = num + 2
print(f'result= ={result}')

# 이해하는 용도로만, 아니면 남이한 코드 수정 용도로만 활용
result2 = num * 2 if num >= 5 else num + 2

print(f'result={result2}')