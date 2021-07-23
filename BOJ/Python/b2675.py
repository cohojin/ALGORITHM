"""

연속으로 입력했을때 값 나오는 방법 찾아보기! 

"""

# 테스트 케이스 갯수
T = int(input())

# 반복횟수 r , 문자열 s
for i in range(T):
  r,s =map(str,input().split())
  for x in s:
    print(x*int(r),end='')
  print()
