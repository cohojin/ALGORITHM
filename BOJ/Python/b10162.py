time = int(input())

a = 300 # 5분
b = 60 # 1분   
c = 10 # 10초
count_a = 0
count_b = 0
count_c = 0 

count_a = time//a 
time = time%a
count_b = time//b 
time = time%b 
count_c = time//c

if(time%c!=0):
  print(-1)
else:
  print(count_a , count_b ,count_c)
