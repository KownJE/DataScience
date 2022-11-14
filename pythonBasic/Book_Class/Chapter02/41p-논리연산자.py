num1 = 100
num2 = 20

# 두 관계식이 같은지 판단
log_result = num1 >= 50 and num2 <=10
print(log_result)

# 두관계식중 하나라도같은지판단
log_result = num1 >= 50 or num2 <=10
print (log_result)

log_result = num1 >= 50 # 관계식판단
print (log_result)

# 괄호안의관계식판단결과에 대한부정
log_result = not(num1 >= 50)
print(log_result)

# 논리연산자는 and, or, not 명령어로 제공
"""
and, or은 양변에 관계식을 가짐. 
and는 두 관계식이 모두 참이면 True를 반환하고, 
or은적어도 한쪽 관계식이 참이면 True를 반환한다. 
not은 논리형 자료를 대상으로 부정을 적용한 값을 반환한다.
예를 들면 True이면 False를 반환하고, False이면 True를 반환한다
"""