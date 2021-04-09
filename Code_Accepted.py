def Code_Accepted():
    import sys
    input = sys.stdin.readline

    import heapq

    N = int(input().rstrip())
    S = []
    for i in range(N):
        S.append(int(input().rstrip()))

    heapq.heapify(S)
    if len(S) == 1:
        print(0)
        return

    r = 0
    while len(S) > 1:
        a = heapq.heappop(S)
        b = heapq.heappop(S)
        heapq.heappush(S, a+b)
        r += a+b
    print(r)