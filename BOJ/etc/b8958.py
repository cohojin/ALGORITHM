T = int(input())

sum = 0
cnt = 0

for i in range(T):
  answer = list(map(str,input()))
  for j in range(len(answer)):
    if(answer[j]=='O'):
      cnt+=1
    else:
      cnt=0
    sum+=cnt
  print(sum)
  cnt=0
  sum=0
