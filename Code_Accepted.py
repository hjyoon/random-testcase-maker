def Code_Accepted():
    import sys


    n = int(sys.stdin.readline())
    numbers = [int(sys.stdin.readline()) for _ in range(n)]
    k = 1
    while True:
        if len(set(number % 10 ** k for number in numbers)) == n:
            break
        k += 1
    print(k)