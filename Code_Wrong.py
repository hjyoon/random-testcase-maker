ans = None
def Code_Wrong():
    global ans
    import sys
    #sys.stdin = open("input.txt", 'r')
    input = sys.stdin.readline

    N = int(input().rstrip())
    S = list(map(int, input().rstrip().split()))
    O = list(map(int, input().rstrip().split()))

    def dfs(i, s, cmp):
        global ans
        if i == N:
            ans = cmp(ans, s)
            #print(ans)
            return
        for j in range(4):
            if O[j] == 0:
                continue
            O[j] -= 1
            if j == 0:
                dfs(i+1, s+S[i], cmp)
            elif j == 1:
                dfs(i+1, s-S[i], cmp)
            elif j == 2:
                dfs(i+1, s*S[i], cmp)
            else:
                dfs(i+1, s//S[i], cmp)
            O[j] += 1

    ans = float('-inf')
    dfs(1, S[0], max)
    print(ans)

    ans = float('inf')
    dfs(1, S[0], min)
    print(ans)