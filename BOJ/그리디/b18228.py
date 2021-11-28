# -1은 펭귄이 위치한 곳 
n = int(input())

ice_power = list(map(int,input().split())) 
# 펭귄이 위치한 곳의 index를 찾고
idx = ice_power.index(-1)

left = ice_power[:idx]
right = ice_power[idx+1:]

print(min(left) + min(right))
