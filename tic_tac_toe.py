"""
Pozitii pe tabla:
 1 | 2 | 3
 _________
 4 | 5 | 6
 _________
 7 | 8 | 9
"""

def display_board():
    print()
    print('    |    |     ')
    print('  ' + board[1] + ' | ' + board[2] + '  | ' + board[3] + '   ')
    print('---------------')
    print('    |    |     ')
    print('  ' + board[4] + ' | ' + board[5] + '  | ' + board[6] + '   ')
    print('---------------')
    print('    |    |     ')
    print('  ' + board[7] + ' | ' + board[8] + '  | ' + board[9] + '   ')


def human_input(mark):
    while True:
        choice = input("Alege pozitia:")
        if choice.isdigit() and int(choice) < 10 and int(choice) > 0:
            choice = int(choice)
            if board[choice] == " ":
                return choice
            else:
                print("Pozitie ocupata deja.")
        else:
            print("Alege o pozitie valida (1 - 9).")


def winning(mark, board):
    winning_place = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for win_place in winning_place:
        if board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == mark:
            return True

def win_move(i, board, mark):
    temp_board = list(board)
    temp_board[i] = mark
    if winning(mark, temp_board):
        return True
    else:
        return False

def cpu_input(cpu, human, board):
    for i in range(1, 10):
        if board[i] == ' ' and win_move(i, board, cpu):
            return i
    for i in range(1, 10):
        if board[i] == ' ' and win_move(i, board, human):
            return i
    for i in [5, 1, 7, 3, 2, 9, 8, 6, 4]:
        if board[i] == ' ':
            return i

def new_game():
    while True:
        nxt = input('Incepi alt joc?(d/n):')
        if nxt in ['d', 'D']:
            again = True
            break
        elif nxt in ['n', 'N']:
            print('La revedere!')
            again = False
            break
        else:
            print("Alege 'd' sau 'n'.")
    if again:
        print('__________NEW GAME__________')
        main_game()
    else:
        return False


def win_check(human, cpu):
    winning_place = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for win_place in winning_place:
        if board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == human:
            print('Felicitari! Ai castigat!')
            if not new_game():
                return False
        elif board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == cpu:
            print('CPU a castigat!')
            if not new_game():
                return False
    if ' ' not in board:
        print('REMIZA!')
        if not new_game():
            return False
    return True


def user_choice():
    while True:
        inp = input('Alege semnul[X/0]: ')
        if inp in ['x', 'X']:
            print('Ai ales "X".\nJoci primul.')
            return 'x','0'
        elif inp in ['0']:
            print('Ai ales "O".\nCPU joaca primul.')
            return '0','x'
        else:
            print('Alege x sau 0!')

def main_game():
    global board
    play = True
    board = ['', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    human, cpu = user_choice()
    display_board()
    while play:
        if human == 'x':
            x = human_input(human)
            board[x] = human
            display_board()
            play = win_check(human, cpu)
            if play:
                o = cpu_input(cpu, human, board)
                print(f'CPU a ales:{o}')
                board[o] = cpu
                display_board()
                play = win_check(human, cpu)
        else:
            x = cpu_input(cpu, human, board)
            print(f'CPU a ales:{x}')
            board[x] = cpu
            display_board()
            play = win_check(human, cpu)
            if play:
                o = human_input(human)
                board[o] = human
                display_board()
                play = win_check(human, cpu)

if __name__ == '__main__':
    main_game()