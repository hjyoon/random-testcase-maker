def Code_Accepted():
    import sys
    #sys.stdin = open("input.txt", 'r')

    N, K = map(int, input().split())
    tem = list(map(int, input().split()))
    i = 0
    tem_sum = sum(tem[0:K])
    max_sum = tem_sum
    if K == 1:
        print(max(tem))
    else:
        while True:
            tem_sum -= tem[i]
            if i + K >= N:
                break
            tem_sum += tem[i+K]
            if max_sum < tem_sum:
                max_sum = tem_sum
            i += 1
        print(max_sum)