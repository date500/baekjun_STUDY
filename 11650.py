import sys
input = sys.stdin.readline

N = int(input())
point = []

for i in range(N):
    a, b = map(int, input().split())
    if [a, b] not in point:
        point.append([a, b])

M = len(point)

for j in range(M):
    for k in range(M-j-1):
        if point[k][0] > point[k+1][0]:
            point[k], point[k+1] = point[k+1], point[k]
        elif point[k][0] == point[k+1][0]:
            if point[k][1] > point[k+1][1]:
                point[k], point[k+1] = point[k+1], point[k]

for p in range (len(point)):
    print(points[i][0], points[i][1])   
