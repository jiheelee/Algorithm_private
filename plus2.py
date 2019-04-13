import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    num_list = list(map(int,input().split()))
    sum_num = 0
    max_sum = max(num_list)
    for i in range(N):
        sum_num = max(sum_num, 0) + num_list[i]
        max_sum = max(sum_num,max_sum)
        
    print(f'#{tc} {max_sum}')

