def cut(n):
    return 3*(n**2)-(3*n)+1

N = int(input())
i = 1
play = True
while play:
    if N==1:
        print(1)
        break
    elif N<=cut(i+1) and N>cut(i):
        print(i+1)
        play = False
    else:
        i += 1

