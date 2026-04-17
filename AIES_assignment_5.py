import math

board = [' ']*9

def show():
    print()
    for i in range(3):
        print(board[i*3], "|", board[i*3+1], "|", board[i*3+2])
    print()

def win(b, p):
    w = [(0,1,2),(3,4,5),(6,7,8),
         (0,3,6),(1,4,7),(2,5,8),
         (0,4,8),(2,4,6)]
    return any(b[a]==b[b1]==b[b2]==p for a,b1,b2 in w)

def minimax(b, is_ai):
    if win(b,'O'): return 1
    if win(b,'X'): return -1
    if ' ' not in b: return 0

    if is_ai:
        best = -10
        for i in range(9):
            if b[i]==' ':
                b[i]='O'
                best = max(best, minimax(b, False))
                b[i]=' '
        return best
    else:
        best = 10
        for i in range(9):
            if b[i]==' ':
                b[i]='X'
                best = min(best, minimax(b, True))
                b[i]=' '
        return best

def ai_move():
    best = -10
    move = 0
    for i in range(9):
        if board[i]==' ':
            board[i]='O'
            score = minimax(board, False)
            board[i]=' '
            if score > best:
                best = score
                move = i
    board[move]='O'

print("You = X, AI = O")
print("Positions: 1 to 9")

while True:
    show()

    user = int(input("Enter move (1-9): ")) - 1
    if board[user] == ' ':
        board[user] = 'X'
    else:
        print("Invalid move")
        continue

    if win(board,'X'):
        show()
        print("You win!")
        break

    if ' ' not in board:
        show()
        print("Draw!")
        break

    ai_move()

    if win(board,'O'):
        show()
        print("AI wins!")
        break

    if ' ' not in board:
        show()
        print("Draw!")
        break
