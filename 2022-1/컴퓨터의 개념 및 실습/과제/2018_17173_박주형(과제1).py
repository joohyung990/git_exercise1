import math
a=int(input("가로의 길이를 입력하세요:"))
b=int(input("세로의 길이를 입력하세요:"))
c=math.sqrt((a**2)+(b**2))
print("빗변의 길이는 ", c, "입니다.", sep="")