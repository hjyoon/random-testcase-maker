def Code_Accepted():
    ans = 0
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().rstrip().split())
        ans = a + b
        print(ans)