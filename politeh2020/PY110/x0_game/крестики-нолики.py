"""
Игра Крестики-нолики. Для двух человек.

     1    2   3
1  [['.' '.' '.']
2   ['.' '.' '.']
3   ['.' '.' '.']]

"""
import numpy as np

# создание поля для игры с координатной сеткой
def create_field():    
    field = np.full((4,4),'.')
    field[0] = np.arange(0,4)
    field[:,0] = np.arange(0,4)
    field[0,0] = " "
    return field

def turn_peoples(xy_X, xy_0, turn):
    while True:
        print(f"\nХод Игрока {turn % 2 + 1}")
        print(field)
        try:    
            x, y = (int(i) for i in input(f"Введите координаты '{sym[turn % 2]}' в формате XY или X Y: ") if i != ' ')
        except:
            print("Некорректный формат ввода! Попробуйте еще раз.")
            continue
        if (x, y) not in xy_X and (x, y) not in xy_0 and x > 0 and x < 4 and y > 0 and y < 4:
            break
        else:
            print(f"Поле с такими координатами ({x}, {y}) не доступно! Попробуйте еще раз.")
    if turn % 2 == 0:
        xy_X.append((x, y))
        field[xy_X[len(xy_X) - 1][1], xy_X[len(xy_X) - 1][0]] = sym[turn % 2]      
    else:
        xy_0.append((x, y))
        field[xy_0[len(xy_0) - 1][1], xy_0[len(xy_0) - 1][0]] = sym[turn % 2]


# функция проверки наличия выигрышной комбинации
def win(win_pos, xy_X, xy_0, end_game):
    if len(xy_X) > 2 or len(xy_0) > 2:
        for i in range(len(win_pos)):
            if (win_pos[i][0] in xy_X and win_pos[i][1] in xy_X and win_pos[i][2] in xy_X):
                print("Победа Крестиков!!!")
                print(field)
                end_game = False
                break
            if (win_pos[i][0] in xy_0 and win_pos[i][1] in xy_0 and win_pos[i][2] in xy_0):
                print("Победа Ноликов!!!")
                print(field)
                end_game = False
                break
    return end_game

field = create_field()
xy_X = [] # координаты ходов Игрока 1 (Крестики)
xy_0 = [] # координаты ходов Игрока 2 (Нолики)
end_game = True

# список всех возможных выигрышных комбинаций
win_pos = [((1, 1), (1, 2), (1, 3)),
           ((2, 1), (2, 2), (2, 3)),
           ((3, 1), (3, 2), (3, 3)),
           ((1, 1), (2, 1), (3, 1)),
           ((1, 2), (2, 2), (3, 2)),
           ((1, 3), (2, 3), (3, 3)),
           ((1, 1), (2, 2), (3, 3)),
           ((1, 3), (2, 2), (3, 1))]

sym = ['X', '0'] # символы для Игрока 1 и Игрока 2
turn = 0 # ход в игре

while end_game:
    turn_peoples(xy_X, xy_0, turn)
    end_game = win(win_pos, xy_X, xy_0, end_game)
    turn += 1
