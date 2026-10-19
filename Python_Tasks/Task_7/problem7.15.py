import math
import os
import random
import re
import sys
from collections import Counter


def gameOfThrones(s):
    freq = Counter(s)
    odd = sum(count % 2 for count in freq.values())

    return "YES" if odd <= 1 else "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()