def Code_Wrong():
    import sys
    input = sys.stdin.readline

    N = int(input().rstrip())
    S = set()

    for _ in range(N):
        S.add(input().rstrip().split('.')[1])

    j = 1
    while True:
        g = set()
        for i in range(1, j+1):
            t = f'{i/j:.4f}'.split('.')[1][:3]
            g.add(t)
        if S.issubset(g):
            break
        j += 1

    print(j)