# n번방까지 최소 거리 구하기 
n = int(input())

# 처음에 한칸을 차지하고 그다음부터는 6의 배수만큼 칸을 차지한다. 
place = 1 
six = 6 
# 기본적으로 1부터 시작한다 ( 최소1부터 시작 )
sum = 1 

while n>place:
  sum+=1
  place+=six
  six+=6

print(sum)

