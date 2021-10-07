from math import ceil 
import sys
input = sys.stdin.readline

# 값 파싱
x, y = map(int, input().split(" "))
target = (y * 100) // x

# 불가능한 경우 제외하고 방정식 대입
if target >= 99:
    print(-1)
else:
    print(ceil((((target + 1) * x)  - (100 * y)) / (99 - target)))
