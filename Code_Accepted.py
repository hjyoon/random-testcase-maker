n, arr, op, minResult, maxResult = None, None, None, None, None
def Code_Accepted():
    global n, arr, op, minResult, maxResult
    import sys

    # dfs
    def dfs(cur,result):
        global n, arr, op, minResult, maxResult

        if cur == n:
            minResult = min(minResult, result)
            maxResult = max(maxResult, result)
            return

        for i in range(4):
            if not op[i] == 0:
                if i == 0:      # 덧셈
                    tmp = result + arr[cur]
                elif i == 1:    # 뺄셈 
                    tmp = result - arr[cur] 
                elif i == 2:    # 곱셈
                    tmp = result * arr[cur]
                else:           # 나눗셈
                    if result < 0:
                        tmp = -result // arr[cur]
                        tmp = -tmp
                    else:
                        tmp = result // arr[cur]

                op[i] -= 1
                dfs(cur+1, tmp)
                op[i] += 1

    # main
    n = int(input())
    arr = [int(x) for x in sys.stdin.readline().split()]
    op = [int(x) for x in sys.stdin.readline().split()]  # +, -, *, %

    minResult = 1000000000
    maxResult = -1000000000
    dfs(1,arr[0])

    print(maxResult)
    print(minResult)