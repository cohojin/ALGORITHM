T = int(input())

# money (25,10,5,1)

count_a=0 #25
count_b=0 #10
count_c=0 #5
count_d=0 #1 

remainder=[]
for i in range(T):
  a = int(input())
  remainder.append(a)
  
for i in range(T):
  count_a = remainder[i]//25 
  remainder[i]=remainder[i]%25 
  count_b = remainder[i]//10
  remainder[i]=remainder[i]%10 
  count_c = remainder[i]//5
  remainder[i]=remainder[i]%5 
  count_d = remainder[i]//1
  print(count_a,count_b,count_c,count_d)
