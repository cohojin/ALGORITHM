n = int(input())
member = input()

# LL은 한쌍이기 때문에 LL을 L하나로 본다! 
member = member.replace('LL','L')

# 컵홀더는 최대 n개를 넘을 수 없다. 
print(min(n,len(member)+1))
