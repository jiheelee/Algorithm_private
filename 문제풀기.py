import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    persons_score = [list(map(int,input().split())) for i in range(N)]
    max_score = 0
    person_num = 0
    for p in persons_score:
        correct_num = p.count(1)
        if correct_num == max_score:
            person_num += 1
        elif correct_num > max_score:
            person_num = 1
            max_score = correct_num

    print(f'#{tc} {person_num} {max_score}')
