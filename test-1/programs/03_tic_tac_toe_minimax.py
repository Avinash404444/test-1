def show(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def win(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def draw(board):
    return all(" " not in row for row in board)

def minimax(board, ai_turn):
    winner = win(board)
    if winner == "O":
        return 1
    if winner == "X":
        return -1
    if draw(board):
        return 0
    best = -100 if ai_turn else 100
    mark = "O" if ai_turn else "X"
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = mark
                score = minimax(board, not ai_turn)
                board[i][j] = " "
                best = max(best, score) if ai_turn else min(best, score)
    return best

def ai_move(board):
    best, move = -100, None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, False)
                board[i][j] = " "
                if score > best:
                    best, move = score, (i, j)
    if move:
        board[move[0]][move[1]] = "O"

board = [[" "] * 3 for _ in range(3)]
print("You = X, AI = O")
while True:
    show(board)
    try:
        n = int(input("Enter position (1-9): ")) - 1
        if not 0 <= n < 9:
            print("Enter a position from 1 to 9.")
            continue
    except ValueError:
        print("Enter a number.")
        continue
    r, c = divmod(n, 3)
    if board[r][c] != " ":
        print("Invalid Move")
        continue
    board[r][c] = "X"
    if win(board) == "X":
        show(board); print("You Win!"); break
    if draw(board):
        show(board); print("Match Draw"); break
    ai_move(board)
    if win(board) == "O":
        show(board); print("AI Wins!"); break
    if draw(board):
        show(board); print("Match Draw"); break
