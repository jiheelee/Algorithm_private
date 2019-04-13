from itertools import combinations

T = int(input())
num, time = map(int,input().split())
change = []
num_list =[]
for n in str(num):
    change.append(n)
for k in str(num):
    num_list.append(n)
k = len(str(num))
com = []
for i in range(k):
    com.append(i)
com = list(combinations(com,2))
print(com)
result = []
def switch(num_list,cnt):
    global time
    if cnt == time:
        result.append(change)
        return

    for i in range(len(com)):
        change[com[i][0]], change[com[i][1]] = num_list[com[i][1]], num_list[com[i][0]]
        switch(change,cnt+1)
switch(num_list,0)
print(result)