"""
성실한 개미 문제 
"""

location = []

for i in range(10):
  location.append([])
  for j in range(10):
    location[i].append(0)
for i in range(10):
  location[i] = list(map(int,input().split()))

x,y = 1,1

while True:
  if(location[x][y] == 0 ):
    location[x][y] = 9
  elif(location[x][y] == 2):
    location[x][y] = 9
    break
  
  if((location[x][y+1] == 1 and location[x+1][y] == 1)):
    break
  
  if(location[x][y+1] != 1):
    y+=1
  elif (location[x+1][y] !=1):
    x+=1
  
for i in range(10):
  for j in range(10):
    print(location[i][j] , end = ' ')
  print()
