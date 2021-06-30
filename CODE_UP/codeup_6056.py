# 참 거짓이 서로 다를 때에만 True로 계산하는 논리연산인 XOR연산 

a,b = map(int,input().split())
print(bool(a) and not(bool(b)) or not(bool(a))and bool(b))
