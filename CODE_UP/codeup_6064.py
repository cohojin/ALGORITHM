# 파이썬 3항연산자 

"""
[true_value] if [condition] else [false_value] // 파이썬 지원
"""

# 문제 
# 3개의 정수 중 가장 작은 값을 출력 

a,b,c = map(int,input().split())
print((a if (a<b) else b) if ((a if (a<b) else b) < c ) else c)

