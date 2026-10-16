import math
import os
import random
import re
import sys
def solve(s):
    return ' '.join(word.capitalize() for word in s.split(' '))


if __name__ == '__main__':
    s = input()
    result = solve(s)
    if 'OUTPUT_PATH' in os.environ:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
        fptr.write(result + '\n')
        fptr.close()
    else:
        print(result)

