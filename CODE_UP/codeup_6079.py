
"""
시간 초과 문제 
solution : while문 조건을 !=이 아닌 <을 사용 했어야 함
"""
# 문제 
# 1, 2, 3, 4, 5 ... 를 순서대로 계속 더해 합을 만들어가다가,입력된 정수와 같거나 커졌을 때, 마지막에 더한 정수를 출력한다.

n = int(input())
sum=0
value=0

while(sum<n):
  value=value+1
  sum=sum+value
print(value)

