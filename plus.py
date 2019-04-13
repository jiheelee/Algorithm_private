import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    num_list = list(map(int,input().split()))

    sum_list = []
    for i in range(N):
        part = 0
        for j in range(i,N):
            part += num_list[j]
            sum_list.append(part)
   
    print("#",end="")
    print(tc,end=" ")
    print(max(sum_list))
        

