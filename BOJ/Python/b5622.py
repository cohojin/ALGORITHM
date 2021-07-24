"""
! 비효율적인 풀이 

다른 풀이 : 
1. 리스트 = ['ABC','DEF','GHI','JKL'....]
넣고 입력받은 알파벳도 list에 넣는다. 그리고 입력받은 알파벳이 in 리스트안에 있다면 리스트.index(리스트) +3 하면 시간이 나온다.

tip : 
- lower() 함수를 통해 소문자로 받을수있다. 
- upper() 함수를 통해 대문자로도 받을수있다. 
"""


alpha = map(str,input())

alpha_list=[]

sum=0

for i in alpha:
  alpha_list.append(i)
  if(i=='A' or i=='B' or i=='C'):
    sum+=3
  elif(i=='D' or i=='E' or i=='F'):
    sum+=4
  elif(i=='G' or i=='H' or i=='I'):
    sum+=5
  elif(i=='J' or i=='K' or i=='L'):
    sum+=6
  elif(i=='M' or i=='N' or i=='O'):
    sum+=7
  elif(i=='P' or i=='Q' or i=='R' or i=='S'):
    sum+=8
  elif(i=='T' or i=='U' or i=='V'):
    sum+=9
  elif(i=='W' or i=='X' or i=='Y' or i=='Z'):
    sum+=10

print(sum)
