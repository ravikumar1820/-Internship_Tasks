def split_and_join(line):
    k=line.split(" ")
    j="-".join(k)
    return j

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)