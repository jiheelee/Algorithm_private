T = int(input())
for tc in range(1, T+1):
    a = str(input())
    stack = [0]
    for i in a:
        if stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    print(f'#{tc} {len(stack)-1}')