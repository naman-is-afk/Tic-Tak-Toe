"""
Tic-Tac-Toe (Console) - PS No. 45
Rungta International Skills University

Two-player console game on a 3x3 board.
Positions: 1-2-3 (top row), 4-5-6 (middle row), 7-8-9 (bottom row).
Player X always plays first.
"""


def display_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def get_move(board, player):
    while True:
        raw = input(f"Player {player}, enter your move (1-9): ").strip()

        if not raw.isdigit():
            print("Invalid position. Enter a number from 1 to 9.")
            continue

        pos = int(raw)
        if pos < 1 or pos > 9:
            print("Invalid position. Enter a number from 1 to 9.")
            continue

        idx = pos - 1
        if board[idx] not in (str(pos),):
            print(f"Position {pos} is already taken. Choose another position.")
            continue

        return idx


def check_win(board):
    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
        (0, 4, 8), (2, 4, 6),              # diagonals
    ]
    for a, b, c in lines:
        if board[a] == board[b] == board[c]:
            return board[a], (a + 1, b + 1, c + 1)
    return None, None


def check_draw(board):
    return all(cell in ("X", "O") for cell in board)


def play_round():
    board = [str(i) for i in range(1, 10)]
    current_player = "X"
    display_board(board)

    while True:
        idx = get_move(board, current_player)
        board[idx] = current_player
        display_board(board)

        winner, line = check_win(board)
        if winner:
            print(f"Player {winner} wins!")
            print(f"Winning line: {line[0]}-{line[1]}-{line[2]}")
            return

        if check_draw(board):
            print("Board is full after 9 moves.")
            print("It's a draw! No moves left.")
            return

        current_player = "O" if current_player == "X" else "X"


def play_game():
    while True:
        play_round()
        again = input("Play again? (y/n) ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    play_game()