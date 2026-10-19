k = int(input())
rooms = list(map(int, input().split()))

unique_rooms = set(rooms)
print((sum(unique_rooms) * k - sum(rooms)) // (k - 1))