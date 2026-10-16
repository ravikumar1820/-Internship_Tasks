n = int(input())
arr = map(int, input().split())
arr = list(set(arr))
arr.sort()

if len(arr) >= 2:
    print(arr[-2])
else:
    print("No second largest number")