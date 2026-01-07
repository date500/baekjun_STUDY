import sys
from collections import deque

input = sys.stdin.readline

while True :
    stack = []
    text = deque(input().rstrip())
    if text[0] == '.'  and len(text) == 1:
        break

    if text[-1] == '.' :
        for i in range (len(text)):
            a = text.popleft()

            if a == '(' :
                stack.append(0)
            elif a == '[' :
                stack.append(1)
            elif a == ')' :        
                if len(stack)>0 and stack[-1] == 0 :
                    stack.pop()
                else : 
                    stack.append(2)
                    break
            elif a == ']' :
                if len(stack)>0 and stack[-1] == 1:
                    stack.pop()
                else : 
                    stack.append(2)
                    break
            
        if len(stack) == 0:
            print("yes")
        else :
            print ("no")

    else:
        print('no')