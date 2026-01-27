import sys

input = sys.stdin.readline

def merge_sort(array):

    if len(array) <= 1:
        return array
        
    mid = len(array) // 2
    low_arr = merge_sort(array[:mid])
    high_arr = merge_sort(array[mid:])

    merged_arr = []
    l = h = 0

    while l < len(low_arr) and h<len(high_arr):
        if len(low_arr[l]) < len(high_arr[h]):
            merged_arr.append(low_arr[l])
            l +=1
        elif len(low_arr[l]) == len(high_arr[h]):
            if low_arr[l] > high_arr[h]:
                merged_arr.append(high_arr[h])
                h += 1
            else:
                merged_arr.append(low_arr[l])
                l += 1
        else :
            merged_arr.append(high_arr[h])
            h += 1

    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

N = int(input())
word = []

for i in range(N):
    a = input().strip()
    if a not in word: 
        word.append(a)
word = merge_sort(word)

for b in range(len(word)):
    print(word[b])