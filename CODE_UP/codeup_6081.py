# 16진수 문제

"""
int(input(),16)을 통해 a값을 16진수 형태로 바꿔준다. 
"""

# 문제 
# 16진수끼리의 곱하기 

a = int(input(),16)
for i in range(1,16):
  print('%X*%X=%X' %(a,i,a*i))
