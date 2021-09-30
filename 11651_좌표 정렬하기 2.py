import sys
input = sys.stdin.readline

n = int(input())

coordinates = []
for _ in range(n):
    a, b = map(int, input().split(" "))
    coordinates.append([a, b])
    
coordinates.sort(key = lambda x : (x[1], x[0]))

for a, b in coordinates:
    print(a, b)
