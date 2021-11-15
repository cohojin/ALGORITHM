# 조건 : k <= m
n,m,k = map (int , input().split())

# n개의 자연수를 입력 받았다.  
data = list(map(int , input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

result = 0 

while True : 
  for i in range(k):
    if m == 0:
      break
    result += first
    m -= 1
  if m == 0:
    break 
  result += second 
  m -= 1 

print(result)
