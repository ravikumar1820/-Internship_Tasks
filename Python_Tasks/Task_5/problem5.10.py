def swap_case(s):
    p=s.swapcase()
    return p

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)