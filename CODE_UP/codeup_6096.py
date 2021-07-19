"""
바둑알이 깔려 있는 상황이 19 * 19 크기의 정수값으로 입력된다.
십자 뒤집기 횟수(n)가 입력된다.
십자 뒤집기 좌표가 횟수(n) 만큼 입력된다. 단, n은 10이하의 자연수이다.

십자 뒤집기 결과를 출력한다. 
"""


location =[]

for i in range(19):
  location.append([])
  for j in range(19):
    location[i].append(0)

for i in range(19):
  location[i] = list(map(int,input().split()))

n = int(input())

for i in range(n):
  x,y = map(int,input().split())
  for j in range(19):
    if location[x-1][j] == 0:
      location[x-1][j] = 1
    else:
      location[x-1][j] = 0
    if location[j][y-1] == 0:
      location[j][y-1] = 1
    else:
      location[j][y-1] = 0 

for i in range(19):
  for j in range(19):
    print(location[i][j], end =' ')
  print()

