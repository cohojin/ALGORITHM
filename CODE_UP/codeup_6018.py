# codeup 기초100제 6018번 sep사용법 
"""
sep(separation)은 문자열 사이에 sep을 끼워서 출력한다. 
"""
# 문제
# 24시간 시:분 형식으로 시간이 입력될 때, 그대로 출력하는 연습을 해보자

a,b=map(str,input().split(":"))
print(a,b,sep=":")

