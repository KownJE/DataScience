# 문제1 [1, 3, 5, 4, 2]라는 리스트를 [5, 4, 3, 2, 1]로 만들어보자.

lst = [1, 3, 5, 4, 2]
#print(lst)
#lst.sort()  # 오름차순
#print(lst)
lst.sort(reverse = True) # 내림차순
print(lst)