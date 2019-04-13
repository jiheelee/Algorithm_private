 
import sys
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    row_list = [''.join(input().split()) for i in range(N)]
    column_list = []
    for i in range(N):
        a = ""
        for j in range(N):
            a += row_list[j][i]
        column_list.append(a)
    cnt = 0
    
    for i in range(N):
        check = 0
        for j in range(N):
            if row_list[i][j] == "0":
                if check == M:
                    cnt += 1
                check = 0
            elif row_list[i][j] == "1":
                check += 1
        if check == M:
            cnt += 1
        check = 0
        for p in range(N):
            if column_list[i][p] == "0":
                if check == M:
                    cnt += 1
                check = 0
            elif column_list[i][p] == "1":
                check += 1
        if check ==M:
            cnt += 1
        check = 0   
            
        
    print('#{} {}'.format(tc,cnt))