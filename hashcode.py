import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    code = ""
    count = 0
    for i in range(N):
        num_array = str(input())
        if "1" in num_array and count==0:
            code += num_array
            count +=1
    end = 0
    
    for i in range(len(code)-56):
        if code[len(code)-i-1] == "1" and end == 0:
            end = len(code)-i-1
    
    code = code[end-55:end+1]
    code_list = []

    for i in range(8):
        code_list.append(code[7*i:7*i+7])
    secret_dict = {
        '0001101':0,
        '0011001':1,
        '0010011':2,
        '0111101':3,
        '0100011':4,
        '0110001':5,
        '0101111':6,
        '0111011':7,
        '0110111':8,
        '0001011':9
    }
    num = ""
    for i in range(len(code_list)):
        code_list[i] = secret_dict[code_list[i]]
    odd = 0
    even = 0
    for i in range(len(code_list)):
        if i % 2:
            even += code_list[i]
        else:
            odd += code_list[i]
    print("#",end="")
    print(tc, end=" ")
    if (3 * odd + even) % 10:
        print(0)
    else:
        print(odd+even)



    

