import sys
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    num = list(map(int,input().split()))
    print(num)
    dan = []
    for i in range(N-1):
        for j in range(1,N-i):
            
            a = num[i] * num[i+j]
            b = '{}'.format(a)
            print(b)
            max_idx = 0
            for i in range(len(b)):
                if int(b[i]) > int(b[max_idx]):
                    max_idx = i
            # if max_idx == (len(a)-1):
            #     dan.append(a)
            # print(dan)