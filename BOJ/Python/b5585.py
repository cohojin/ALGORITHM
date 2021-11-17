pay = int(input())

remain_money = 1000-pay 
count = 0
sum = 0

money=[500,100,50,10,5,1]

for i in range(6):
  if(remain_money//money[i]!=0):
    count= remain_money//money[i]
    remain_money=remain_money%money[i]
    sum+=count
    if(remain_money==0):
      break

print(sum)

