import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    A,B,C = map(int,input().split())
    m = min(A,B)
    print(f'#{tc} {C//m}')