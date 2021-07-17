# 문제 
# 첫 번째 줄에 출석 번호를 부른 횟수인 정수 n이 입력된다. (1 ~ 10000) 두 번째 줄에는 무작위로 부른 n개의 번호(1 ~ 23)가 공백을 두고 순서대로 입력된다.

n = int(input())
a = list(map(int,input().split()))
d = []

for i in range(24):
  d.append(0)
for i in range(n):
  d[a[i]] += 1
for i in range(1,24):
  print(d[i] , end=' ')

