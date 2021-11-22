n = int(input())

hills = list(map(int , input().split()))

sum = 0
maxHill = 0 #기준값
cnt = 0

for i in hills:
    if i > maxHill:
        maxHill = i
        cnt = 0
    else:
        cnt +=1
    sum = max(sum , cnt)

print(sum)
