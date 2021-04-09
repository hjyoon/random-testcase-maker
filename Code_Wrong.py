def Code_Wrong():
    import sys
    input = sys.stdin.readline

    import itertools

    N = int(input().rstrip())
    S = []
    for i in range(N):
        S.append(int(input().rstrip()))

    S.sort()

    t = list(itertools.accumulate(S, lambda x,y:x+y))
    print(sum(t[1:]))
    pass