# (1) value 인수
print("value =", 10 + 20 + 30 + 40 + 50)

# (2) sep 인수 ： 값과 값을 특수문자로 구분
print("010", "1234", "5678", sep="-")

# (3) end 인수
print("value=", 10, end = ", ")
print("value=", 20)


# print() 함수는 5개의 인수를 사용할 수 있다.
# values, sep, end 등의 인수를 자주 사용하고,
# file, flush 인수는 자주 사용되지 않는다