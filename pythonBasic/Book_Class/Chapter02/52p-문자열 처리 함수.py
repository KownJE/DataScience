# (1) 특정글자수 반환
oneLine = "this is one line string"
print ('t 글자수 : ', oneLine.count ('t'))

# (2) 접두어 문자 비교 판단
print (oneLine. startswith ('this'))
print (oneLine. startswith ('that'))

# (3) 문자열 교체
print(oneLine.replace ('this', 'that')) # replace() 함수는 '' , '' 왼쪽을 오른쪽으로 교체함

# (4) 문자열 분리(split) ：문단 -> 문장
multiLine = """this is
multi line 
string"""
sent = multiLine.split('\n') # split () 함수는 줄바꿈('\n') 구분자를 기준으로 문자열을 분리한다
print ('문장 ：', sent)

# (5) 문자열 분리 (split) 2 : 문장 -> 단어
words = oneLine.split(' ') # split () 함수는 공백(' ') 구분자를 기준으로 문자열을 분리한다
print('단어 ：', words)

# (6) 문자열 결합(join) : 단어 -> 문장
sent2 = ','.join(words) #  '구분자'.join(string)
print(sent2) # joino() 함수는구분자콤마(,)를 기준으로 다시하나의 문자열로 결합한다