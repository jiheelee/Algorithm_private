T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split())
    num_list = []
    for i in range(E):
        num_list.extend(list(map(int,input().split())))
    S, G = map(int,input().split())
    node = [[] for i in range(V+1) ]
    for i in range(len(num_list)//2):
        node[num_list[2*i]].append(num_list[2*i+1])
        # node[num_list[2*i+1]].append(num_list[2*i])
        for j in node:
            if num_list[2*i] in j:
                j.append(num_list[2*i+1])
    for i in range(len(num_list)//2):    
        for j in node:
            if num_list[2*i] in j:
                j.append(num_list[2*i+1])
    result = 0
    
    if G in node[S]:
        result = 1
    print(f'#{tc} {result}')   