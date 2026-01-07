import sys
input = sys.stdin.readline

stack = []
printlist = []

N = int(input())

for i in range (N):
    command = input().split()

    if command[0] == 'push' :
        num = int(command[1])
        stack.append(num)
        
    elif command[0] == 'pop':
        if len(stack) == 0: 
            printlist.append(-1)
        else:
            a = stack.pop()
            printlist.append(a)

    elif command[0] == 'size' :
        printlist.append(len(stack))

    elif command[0] == 'empty' :
        if len(stack) == 0 :
            printlist.append (1)
        else:
            printlist.append (0)

    elif command[0] == 'top' :
        if len(stack) == 0:
            printlist.append(-1)
        else:
            printlist.append(stack[-1])

for j in range (len(printlist)):
    print(printlist[j])