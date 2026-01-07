import sys
input = sys.stdin.readline

N, M = map(int, input().split())
i=0
num = []
sumlist = [0]
temp_sum = 0

num = list(map(int, input().split()))

for i in num :
    temp_sum = temp_sum + i
    sumlist.append(temp_sum)

result= []
for j in range (M) :
    start, fin = map(int, input().split())
    result.append(sumlist[fin] - sumlist[start-1])

for a in range (M):
    print(result[a])
    a = a + 1