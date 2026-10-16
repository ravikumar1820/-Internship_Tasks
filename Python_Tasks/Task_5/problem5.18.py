def minion_game(string):
    stuart = 0
    kevin = 0
    n = len(string)

    for i in range(n):
        if string[i] in 'AEIOU':
            kevin += n - i
        else:
            stuart += n - i

    if stuart > kevin:
        print("Stuart", stuart)
    elif kevin > stuart:
        print("Kevin", kevin)
    else:
        print("Draw")
    

if __name__ == '__main__':
    s = input()
    minion_game(s)