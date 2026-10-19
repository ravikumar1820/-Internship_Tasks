import math
import os
import random
import re
import sys
from collections import Counter
def isValid(s):
    freq = Counter(Counter(s).values())

    if len(freq) == 1:
        return "YES"

    if len(freq) == 2:
        f1, f2 = freq.keys()

        if (freq[f1] == 1 and (f1 - 1 == f2 or f1 == 1)):
            return "YES"

        if (freq[f2] == 1 and (f2 - 1 == f1 or f2 == 1)):
            return "YES"

    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
