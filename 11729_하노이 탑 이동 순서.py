def hanoi(start, temp, end, n):
    global lines
    
    if n == 1:
        lines.append([start, end])
        
        return 1
    else:
        count = 0
        count += hanoi(start, end, temp, n - 1)
        count += hanoi(start, temp, end, 1) 
        count += hanoi(temp, start, end, n - 1)
        
        return count
    

n = int(input())

global lines
lines = []

print(hanoi(1, 2, 3, n))
for a, b in lines:
    print(a, b)
