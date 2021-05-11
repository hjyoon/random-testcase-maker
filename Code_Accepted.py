def Code_Accepted():
    n = int(input())
    float_list = []
    for i in range(n):
        float_list.append(float(input()))
    answer = 1000
    for k in range(1, 1001):
        flag = True
        for number in float_list:
            left = k * number
            right = k * (number + 0.001)
            if left == int(left) or (right != int(right) and int(right) != int(left)):
                continue
            flag = False
            break
        if flag:
            answer = k
            break
    print(answer)