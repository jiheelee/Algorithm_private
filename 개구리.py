import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    stones = list(map(int,input().split()))
    K = int(input())
    i = 0
    cnt = 0
    result = 0
    for a in range(N):
        check = 0
        i = i + K
        if i in stones:
            cnt += 1
            check = 1
        else:
            back = 0
            while back <= K-2:
                i -= 1
                if i in stones:
                    cnt += 1
                    check =1
                    break
                back += 1
        if check == 0:
            result = -1
            break
        if i >= stones[-1]:
            break
    if result == -1:
        print(result)
    else:
        print(cnt)