from sys import stdin

input = stdin.readline

def get_num(a):
    for i in range(n):
        if not is_use[i]:
            big = i

    for i in range(n):
        if not is_use[i] and num_list[i]:
            big = compare_pri(big, i, a)
    
    is_use[big] = True
    return big

def compare_pri(a, b, c):
    a_val = num_list[a]
    b_val = num_list[b]
    
    for i in range(100):
        if len(a_val) < i + 1:
            is_use[a] = True
            next_n = get_num(c)
            a_val += num_list[next_n]
            is_use[next_n] = False
            is_use[a] = False
        if len(b_val) < i + 1:
            is_use[b] = True
            next_n = get_num(c)
            b_val += num_list[next_n]
            is_use[next_n] = False
            is_use[b] = False
        if a_val == b_val:
            return a
        if int(a_val[i]) > int(b_val[i]):
            return a
        elif int(a_val[i]) < int(b_val[i]):
            return b
        
ans = ''
n = int(input())
num_list = list(map(str, input().split()))
is_use = [False for i in range(n)]

for i in range(n):
    ans += num_list[get_num(i)]
    
print(int(ans))
