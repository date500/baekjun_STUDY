import sys
from collections import deque
input = sys.stdin.readline

queue = deque([])
printlist = []

N = int(input())

for i in range (N):
    command = input().split()

    if command[0] == 'push' :
        num = int(command[1])
        queue.append(num)
        
    elif command[0] == 'pop':
        if len(queue) == 0: 
            printlist.append(-1)
        else:
            a = queue.popleft()
            printlist.append(a)

    elif command[0] == 'size' :
        printlist.append(len(queue))

    elif command[0] == 'empty' :
        if len(queue) == 0 :
            printlist.append (1)
        else:
            printlist.append (0)

    elif command[0] == 'front' :
        if len(queue) == 0:
            printlist.append(-1)
        else:
            printlist.append(queue[0])
    
    elif command[0] == 'back' :
        if len(queue) == 0:
            printlist.append(-1)
        else:
            printlist.append(queue[-1])

for j in range (len(printlist)):
    print(printlist[j])