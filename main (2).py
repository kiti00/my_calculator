import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    # Перевірка рядків, стовпців і діагоналей
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(cell != " " for row in board for cell in row)

def player_move(board):
    while True:
        try:
            move = int(input("Введіть номер клітинки (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("Клітинка зайнята! Спробуйте ще раз.")
        except (ValueError, IndexError):
            print("Некоректний ввід. Введіть число від 1 до 9.")

def computer_move(board):
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = "O"

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Гра 'Хрестики-нулики'! Ви граєте за X.")
    print_board(board)

    while True:
        player_move(board)
        print_board(board)
        if check_win(board, "X"):
            print("Ви виграли!")
            break
        if check_draw(board):
            print("Нічия!")
            break

        print("Хід комп'ютера...")
        computer_move(board)
        print_board(board)
        if check_win(board, "O"):
            print("Комп'ютер виграв!")
            break
        if check_draw(board):
            print("Нічия!")
            break

if __name__ == "__main__":
    main()
