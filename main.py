import os

PLAYER_1 = "X"
PLAYER_2 = "O"


def main():
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    print_board(board)

    for _ in range(5):  # Modified loop to allow 5 moves in total
        for player in (PLAYER_1, PLAYER_2):
            move = input("Enter move: ")

            try:
                board = parse_input(board, move, player)

            except ValueError as e:
                print(e)
                exit()

            print_board(board)
            winner = check_win(board)
            if winner:
                print(f"Player {winner} wins!")
                return  # End the game if there's a winner

    print("It's a draw!")  # No winner after all moves


def check_win(board: list):
    patterns = [
        ((1, 1), (2, 1), (0, 1)),  # middle vertical column check
        ((1, 1), (1, 0), (1, 2)),  # middle horizontal column check
        ((1, 1), (2, 2), (0, 0)),  # diagonal \ check
        ((1, 1), (2, 0), (0, 2)),  # diagonal / check
        ((0, 0), (1, 0), (2, 0)),  # left vertical check
        ((0, 0), (0, 1), (0, 2)),  # top horizontal check
        ((2, 2), (0, 2), (1, 2)),  # right vertical check
        ((2, 2), (2, 1), (2, 0))  # bottom horizontal check
    ]

    for i in (PLAYER_1, PLAYER_2):
        for pattern in patterns:
            if all(board[pos[0]][pos[1]] == i for pos in pattern):
                return i
    return None


def print_board(board: list):
    os.system("clear")

    print("  -------------------")

    for row_i, row in enumerate(board, start=1):
        print(f"{row_i}|  ", end="")
        for col in row:
            print(
                f"{col}  |".replace(str(PLAYER_1), "X")
                .replace(str(PLAYER_2), "O"),
                end="  "
            )

        print()

    print("  -------------------")
    print("    a     b     c")


def parse_input(board: list, value: str, player) -> list:
    if len(value) != 2:
        raise ValueError("Input Error")

    a, b = value[0], int(value[1]) - 1

    if a not in ('a', 'b', 'c') or b not in (0, 1, 2):
        raise ValueError("Input Error")

    match a:
        case 'a':
            board[b][0] = player
            return board
        case 'b':
            board[b][1] = player
            return board
        case 'c':
            board[b][2] = player
            return board


if __name__ == '__main__':
    main()
