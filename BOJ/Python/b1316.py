#n개의 문자를 입력받고 그 값을 result에 넣어서 빼기
n = int(input())
result = n 

for i in range(n):
  word=input()
  for j in range(0,len(word)-1):
    if word[j] == word[j+1]:
      pass
    # word[j]가 나머지에서 같은게 있으면 
    elif word[j] in word[j+1:]:
      result -=1 
      break
print(result)
