# (1) 문자형 숫자 입력
num = input ("숫자 입력 : ")          # input에 입력할 경우 콘솔에 출력되는 메시지 역할을 한다.
print ('num type ： ', type (num)) # <class 'str' >
print (' num = ', num)
print ('num = ', num * 2)     # 문자형이기 때문에 연산이 불가능/ 곱하는게 아니라 문자열을 2회 반복

# (2) 문자형 숫자를 정수형으로 변환
num1 = int ( input ("숫자 입력 : ")) # str -> int(형변환)
print('num1 = ', num1 * 2)

# (3) 문자형 숫자를 실수형으로 변환
num2 = float (input ("숫자 입력 : ")) # str -> float(형변환)
result = num1 + num2 # 실수 = 정수 + 실수
print('result = ', result)
