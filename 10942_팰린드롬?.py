import sys
input = sys.stdin.readline

# 입력
n = int(input())
nums = list(map(int, input().split(" ")))

# 쿼리 중복 연산을 막기 위한 dp 계산
dp = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][i] = 1
for i in range(n - 1):
    if nums[i] == nums[i + 1]:
        dp[i + 1][i + 2] = 1

# 경우의 수 순회
for s in range(2, n):
    for e in range(1, n - s + 1):
        if dp[e + 1][e + s - 1] == 1 and nums[e - 1] == nums[e + s - 1]:
            dp[e][e + s] = 1
            
# 쿼리 입력
m = int(input())
for i in range(m):
    s, e = map(int, input().split(" "))
    
    print(dp[s][e])
