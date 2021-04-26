def Code_Wrong():
    import sys
    #sys.stdin = open("input.txt", 'r')
    input = sys.stdin.readline

    N, K = map(int, input().rstrip().split())
    L = list(map(int, input().rstrip().split()))
    l = []
    r = float('-inf')
    for i in range(N):
        if len(l) == 0:
            l.append(L[i])
        else:
            l.append(l[i-1] + L[i])

    for i in range(K-1, N):
        if i-K >= 0:
            r = max(r, l[i]-l[i-K])
            #print(l[i]-l[i-K])
        else:
            r = max(r, l[i])
            #print(l[i])

    print(r)