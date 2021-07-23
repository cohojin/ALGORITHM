"""

다른 풀이 : 
1. reverse 함수를 이용하면 리스트 안에 내용들이 역순으로 배치된다.
2. 리스트 슬라이싱을 이용 
ex) 입력받은 변수 a를 거꾸로 변환시키려면 a[::-1] 
단 , 문자열로 입력받은 변수만 슬라이싱 할 수 있다. 

"""

a,b = map(int,input().split())

list_a = []
list_b = [] 

for i in str(a):
  list_a.append(i)
for i in str(b):
  list_b.append(i)

m = list_a[2]+list_a[1]+list_a[0]
n = list_b[2]+list_b[1]+list_b[0]

if(m>n):
  print(m)
else:
  print(n)


