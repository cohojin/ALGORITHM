n = int(input())

# 0은 딸기우유 , 1은 초코우유 , 2는 바나나우유

milk = list(map(int,input().split()))

# 0을 먼저 찾고 count 올리고 그다음 1을 찾고 count 올리고 ,,, 

count = 0

for i in range(n):
  if(milk[i] == count%3):
    count+=1

print(count) 
