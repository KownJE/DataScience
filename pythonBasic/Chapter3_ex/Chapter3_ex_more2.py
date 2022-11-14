# 추가문제 3
import math

arr = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

result = sum(arr)# 합계 구하기=> sum(리스트)
print(f"average : {result / len(arr)}")

# 소수점 빼고 싶어서 만들어봄
arr2 = [75, 82, 90, 77, 64, 55, 48, 70, 88, 100]

result2 = sum(arr2)
print(f"average2 : {result2 / len(arr2)}") # => 74.9 값이 나옴
x = math.floor(result2 / len(arr2)) # 소수점 아랫 숫자 다내림
y = round(result2 / len(arr2))      # 소수점 아래의 숫자를 반올림하여 출력

print(x)
print(y)

#---------------------------------------------------------------
