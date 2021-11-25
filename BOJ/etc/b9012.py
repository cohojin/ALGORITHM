t = int(input())

ps_list = ["(",")"]

for j in range(0,t):

  cnt = 0

  ps = map(str,input())
  ps= list(ps)

  ps_len = len(ps)    
  ps_list_len = len(ps_list)

  for i in range(0,ps_len):
    if(ps_list[0]==ps[i]):
      cnt+=1
    elif(ps_list[1]==ps[i]):
      cnt-=1

    if(cnt==-1):
      break

  if(cnt==0):
    print("YES")
  else:
    print("NO") 
