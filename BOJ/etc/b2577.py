num= list( int(input()) for i in range(3))

result_list = list(str(num[0]*num[1]*num[2]))

for i in range(10):
  i=str(i)
  print(result_list.count(i))
