# 색인의 범위를 이용하여 특정 문자열을 대상으로 부분 문자열을 생성하는 것

# 문자열[시작색인 : 끝색인 : 증감값]   <== 형식

oneLine = "this is one line string"
# ⑴ 왼쪽 기준
print(oneLine)
print("문자열 길이 : ", len(oneLine) )
print(oneLine[0 : 4])
print(oneLine[:4])
print(oneLine [:]) # 전체 원소
print(oneLine[::2]) # 2의 배수 index 전체를 대상으로 색인이 2씩 증가하여 슬라이싱

# (2) 오른쪽 기준
print (oneLine [0:-1:2]) # 왼쪽 처음부터 오른쪽 끝 이전까지 2씩 증가하여 슬라이싱
print (oneLine [-6:-1]) # 오른쪽 맨끝을 기준으로 6번째문자부터 마지막문자 이전까지 슬라이싱
print (oneLine [-6:]) # 오른쪽 맨 끝을 기준으로 6번째 문자부터 마지막 문자까지 슬라이싱

# (3) 부분 문자열 생성
substring = oneLine[-11: ] # 오른쪽 맨 끝을 기준으로 11번째 문자에서 마지막 문자까지 슬라이싱
print(substring)