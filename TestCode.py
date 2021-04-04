import sys
import os
import filecmp

def Accepted_Code():
    from collections import deque
   
    def solve(n,m) :
        snake = [0 for _ in range(101)]
        ledder = [0 for k in range(101)]
        #합쳐서 관리하는게 더 나을 것 같다.
        
        visited = [False for _ in range(101)]

        for i in range(n) :
            x , y = map(int,input().split())
            ledder[x] = y
        
        for j in range(m) :
            x , y = map(int,input().split())
            snake[x] = y

        q = deque()

        q.append((1,0))
        visited[1] = True

        ans = float("inf")

        while q :
            
            front = q.popleft()

            if front[0] == 100 :
                ans = min(ans, front[1])
                continue


            for i in range(1,7) :
                new = front[0]+i
                
                if new > 100 :continue
                
                if visited[new] == True :
                    continue
                
                visited[new] = True

                if snake[new] != 0 :
                    new = snake[new]
                
                if ledder[new] != 0 :
                    new = ledder[new]

                q.append((new,front[1]+1))
        
        print(ans)
            
            

    n,m = map(int,input().split())
    solve(n,m)
    pass

def Wrong_Answer_Code():
    N, M = map(int, input().rstrip().split())
    m = [0]*101
    r = [999999]*101
    for i in range(N+M):
        x, y = map(int, input().rstrip().split())
        m[x] = y

    def go(now, step):
        #print(now, step)
        if now > 100:
            return
        if step >= r[now]:
            return
        r[now] = step
        if m[now] != 0:
            go(m[now], step)
            return
        if now == 100:
            return
        for i in range(1, 7):
            go(now+i, step+1)

    go(1, 0)
    #print(*r)
    print(r[100])
    pass

input_path = "output_testcase/"
output_path = "result_testcase/"
extension = ".txt"
input_file_name_base = "output_case_"
accepted_output_file_name_base = "_result_by_case_accepted"
wrong_output_file_name_base = "_result_by_case_wrong"
F = 1000
T = 1

if not os.path.exists(input_path):
    os.makedirs(input_path)

if not os.path.exists(output_path):
    os.makedirs(output_path)

for i in range(1, F+1):
    input_file_name = f'{input_path}{input_file_name_base}{i}{extension}'
    accepted_in_f = open(input_file_name, 'r')
    wrong_in_f = open(input_file_name, 'r')

    accepted_output_file_name = f'{output_path}{i}{accepted_output_file_name_base}{extension}'
    accepted_out_f = open(accepted_output_file_name, 'w')

    wrong_output_file_name = f'{output_path}{i}{wrong_output_file_name_base}{extension}'
    wrong_out_f = open(wrong_output_file_name, 'w')

    for j in range(T):
        tmp = sys.stdout
        tmp2 = sys.stdin
        sys.stdout = accepted_out_f
        sys.stdin = accepted_in_f
        Accepted_Code()
        sys.stdout = wrong_out_f
        sys.stdin = wrong_in_f
        Wrong_Answer_Code()
        sys.stdout = tmp
        sys.stdin = tmp2

    accepted_in_f.close()
    wrong_in_f.close()
    accepted_out_f.close()
    wrong_out_f.close()

    if filecmp.cmp(accepted_output_file_name, wrong_output_file_name):
        #print(f'case #{i}: OK')
        pass
    else:
        input_file_name = f'{input_path}{input_file_name_base}{i}{extension}'
        testcase_in_f = open(input_file_name, 'r')
        accepted_out_f = open(accepted_output_file_name, 'r')
        wrong_out_f = open(wrong_output_file_name, 'r')
        print(f'case #{i}: ERR')
        print('input:')
        print(*testcase_in_f.readlines(), sep='')
        print()
        print('accepted:')
        print(*accepted_out_f.readlines(), sep='')
        print('wrong answer:')
        print(*wrong_out_f.readlines(), sep='')
        accepted_out_f.close()
        wrong_out_f.close()
        pass