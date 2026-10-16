from collections import Counter

n = int(input())
words = []

for i in range(n):
    words.append(input())

frequency = Counter(words)

print(len(frequency))
print(*frequency.values())