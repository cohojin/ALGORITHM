# 1보다 크거나 같고 n보다 작거나 같은 x
x = int(input())
# 갯수 출력 
count=0

for i in range(1,x+1):
  num_list = list(map(int,str(i)))
  if i <100:
    count+=1
  elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
    count+=1
print(count)
