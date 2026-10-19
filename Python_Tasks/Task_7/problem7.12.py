import math
import os
import random
import re
import sys
from collections import Counter


def makingAnagrams(s1, s2):
     c1 = Counter(s1)
     c2 = Counter(s2)

     count = 0

     for ch in set(c1) | set(c2):
         count += abs(c1[ch] - c2[ch])

     return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
