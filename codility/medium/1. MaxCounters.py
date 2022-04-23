# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):

    result = [0] * N
    max_count = 0
    add_max = 0
    for i, v in enumerate(A):
        if v >= 1 and v <= N:
            #더해 줄 값보다 작으면 더해줄 값을 +해준다.
            if result[v - 1] < add_max:
                result[v - 1] = add_max + 1
            else:
                result[v - 1] += 1
            max_count = max(max_count, result[v - 1])
            continue

        if v == N + 1:
            #더해 줄 값을 재세팅해준다.
            add_max = max_count

    
    for i, v in enumerate(result):
        #마지막으로 더해줄 값보다 작으면 add_max로 재세팅해준다.
        if v < add_max:
            result[i] = add_max

    return result




    # 시간초과로 77점
    # write your code in Python 3.6
    result = [0] * N
    max_count = 0

    for i, v in enumerate(A):
        if v >= 1 and v <= N:
            result[v - 1] += 1
            max_count = max(max_count, result[v - 1])

        if v == N + 1:
            result = [max_count] * N
    return result
