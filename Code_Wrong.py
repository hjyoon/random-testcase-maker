def Code_Wrong():
    import sys
    input = sys.stdin.readline

    N, *S = list(map(lambda x:x.rstrip(), sys.stdin))

    left = 1 
    right = len(S[0])
    mid = 0
    res = 0

    def chk():
        s = set()
        for v in S:
            s.add(v[len(S[0])-mid:])
        if len(s) == len(S):
            return True
        else:
            return False

    while left <= right:
        mid = (left + right) // 2
        if chk():
            #print(left, right, mid, 'True')
            res = mid
            right = mid - 1
        else :
            #print(left, right, mid, 'False')
            left = mid + 1

    print(res)