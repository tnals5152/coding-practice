
def main():
    m, n = map(int, input().split())
    min_count = 8 * 8#다시 다 칠해야 되는 경우로 세팅
    chess = []
    for _ in range(m):
        chess.append(input())



    for y in range(0, m - 8 + 1):
        for x in range(0, n - 8 + 1):
            #0 ~ 7, 0 ~ 7라인까지 갖도록 ->이제 번갈아서 있는지 체크
            #다시 색칠해야 되는 개수 구함 -> 8 * 8 /2보다 크면 8 * 8 - 구한 값
            start = chess[y][x]
            count = 0
            for b in range(y, y + 8):
                for a in range(x, x + 8):
                    if chess[b][a] == start and not \
                        ((b % 2 == 0 and a % 2 == 0) or
                        (b % 2 == 1 and a % 2 == 1)):
                        count += 1

                    elif chess[b][a] != start and not \
                        ((b % 2 == 1 and a % 2 == 0) or
                        (b % 2 == 0 and a % 2 == 1)):
                        count += 1

            if count > (8 * 8) // 2:
                count = 8 * 8 - count
            min_count = min(min_count, count)

    print(min_count)

main()
