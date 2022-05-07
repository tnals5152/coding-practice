move = {
    "R": (1, 0),
    "L": (-1, 0),
    "B": (0, -1),
    "T": (0, 1),
    "RT": (1, 1),
    "LT": (-1, 1),
    "RB": (1, -1),
    "LB": (-1, -1),
}
chess_len = 8

def main():
    king_position, stone_position, count = input().split()
    king_position = find_position(king_position)
    stone_position = find_position(stone_position)
    

    for _ in range(int(count)):
        x, y = move[input()]

        #범위 넘어갔을 시 contiue
        if not position_check(king_position, x, y):
            continue
        
        #돌이 있는 곳으로 이동할 때
        if king_position[0] + x == stone_position[0] and\
            king_position[1] + y == stone_position[1]:
            #돌과 같이 움직이는데 -> 돌이 체스판 밖으로 나가면 킹도 움직임 X
            if not position_check(stone_position, x, y):
                continue
            stone_position = move_position(stone_position, x, y)
        king_position = move_position(king_position, x, y)
    
    print(get_position(king_position))
    print(get_position(stone_position))

def find_position(position):
    x = ord(position[0]) - 65
    y = int(position[1]) - 1
    return [x, y]

def get_position(position):
    return chr(position[0] + 65) + str(position[1] + 1)

def position_check(position, x, y):
    if position[0] + x >= chess_len or position[0] + x < 0 or\
        position[1] + y >= chess_len or position[1] + y < 0:
        return False
    return True

def move_position(position, x, y):
    return [position[0] + x, position[1] + y]

main()
