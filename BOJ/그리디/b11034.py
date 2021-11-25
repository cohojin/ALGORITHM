while True:
  try: 
    a,b,c = map(int,input().split())
    count_a = c-b-1 
    count_c = b-a-1 
    print(max(count_a,count_c))
  except:
    break
