"""

1. alpha[]에 range()를 이용해서 아스키코드 알파벳 숫자 범위를 넣었다. 
2. chr 함수 => 아스키코드에 해당하는 숫자를 문자열로 변환시키는 함수이다. 
@ 문자를 숫자(아스키코드)로 변환할 때는 ord()함수를 이용한다. 
3. find 함수는 문자열에서만 사용 가능한 함수이다. 
find는 찾는 문자가 문자열안에 포함되지 않은 경우는 -1을 출력한다. 
@ find 함수와 유사한 기능을 하는 함수로 index 함수가 존재한다. index 함수는 문자가 문자열 안에 포함되지 않은 경우에 AttributeError가 발생한다. 

"""


s = input()

# 입력된 단어 위치 찾기 

alpha = list(range(97,123))

for x in alpha:
  print(s.find(chr(x)) , end= ' ')

  
