word = list(input()) 

count = 0 
start = "A" 

for i in word: 
  left = ord(i) - ord(start) 
  right = ord(start) - ord(i) 

  if left < 0:
    left += 26 
  elif right <0:
    right +=26 
    
  count += min(left,right)
  start = i

print(count)
