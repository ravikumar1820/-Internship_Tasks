import math
import os
import random
import re
import sys
def anagram(s):
    n = len(s)
    if n % 2 != 0:
        return -1
    mid = n // 2
    s1 = s[:mid]
    s2 = s[mid:]
    from collections import Counter
    c1 = Counter(s1)
    c2 = Counter(s2)
    return sum((c1 - c2).values())
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = anagram(s)
        fptr.write(str(result) + '\n')
    fptr.close()
