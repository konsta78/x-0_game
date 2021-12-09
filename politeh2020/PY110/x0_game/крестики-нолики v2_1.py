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

def turn_peoples(xy, turn):
    while True:
        print(f"\nХод Игрока {turn % 2 + 1}")
        print(field)
        try:    
            x, y = (int(i) for i in input(f"Введите координаты '{sym[turn % 2]}' в формате XY или X Y: ") if i != ' ')
        except ValueError:
            print("Некорректный формат ввода! Попробуйте еще раз.")
            continue
        if (x, y) not in xy[0] and (x, y) not in xy[1] and 0 < x < 4 and 0 < y < 4:
            break
        else:
            print(f"Поле с такими координатами ({x}, {y}) не доступно! Попробуйте еще раз.")   
    xy[turn%2].append((x,y))
    field[xy[turn%2][-1][1], xy[turn%2][-1][0]] = sym[turn % 2]
    print(field)

# функция проверки наличия выигрышной комбинации
def win(win_pos, xy, end_game, turn):
    if 2 < len(xy[0]) < 5: # проверка на выигрыш начинается только после третьего хода 'X' и до 5-го
        for i, j in enumerate(win_pos):
            if j[0] in xy[turn%2] and j[1] in xy[turn%2] and j[2] in xy[turn%2]:
                end_game = False
                print(f"Игрок {turn%2 + 1} Выиграл!. Победа '{sym[turn % 2]}'")
                break
    elif len(xy[0]) == 5:
        print("Ничья! Победила дружба :)")
        end_game = False
    return end_game

field = create_field()
xy = [[],[]] # список коорлинат для 'Х' и для '0'
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
    turn_peoples(xy, turn)
    end_game = win(win_pos, xy, end_game, turn)
    turn += 1
