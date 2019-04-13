import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N,M,C = map(int,input().split())
    room = [list(map(int,input().split())) for i in range(N)]
    mul = []
    for i in range(N):
        for j in range(N-M+1):
            A = []
            for m in range(M):
                A.append(room[i][j+m])
            total_list = []
            for s in range(1<<M):
                subset_list = []
                for k in range(M+1):
                    if s & (1<<k):
                        subset_list.append(A[k])
                        cnt+=1
                if cnt == 3:
                    
                total_list.append(subset_list)
            max_num = 0
            for l in total_list:
                if sum(l)<=C:
                    x = 0
                    for z in l:
                        x += z ** 2
                    if x >= max_num:
                        max_num = x
            mul.append(max_num)
    
    max_idx = 0
    max_mul = max(mul)
    for idx in range(len(mul)):
        if mul[idx] == max(mul):
            max_idx = idx
    div_num = N-M+1
    for y in range(M-1):       
        if (max_idx + y+1)//div_num == max_idx//div_num:
            mul[max_idx+y+1]=0
        if (max_idx - (y+1))//div_num == max_idx//div_num:
            mul[max_idx-(y+1)]=0    
    mul[max_idx]=0
    max_mul_2 = max(mul)
   
    print(f'#{tc} {max_mul+max_mul_2}')