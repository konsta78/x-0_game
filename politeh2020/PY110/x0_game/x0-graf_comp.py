"""
Игра Крестики-Нолики v 1.0
Первым ходит Человек (нолики)
Вторым - Компьютер (крестики)

TODO: 
    - при открытии доп. окна на продолжение игры остается активным основное окно
      и в нем можно кликать, что сразу вызывает кучу проблем...
    - функция create_field спользует глобальные переменные...
    - надо улучшить ИИ при ходах в углы и в бок
    - оптимизировать логику ИИ: практически два идентичных for
    - в check_win трижды вызывается функция end_game
    
    field:
    1 2 3
    4 5 6
    7 8 9
    
"""

from tkinter import *
import random as r

# начальные настройки
cell = 200 # размер ячейки игрового поля
a = cell // 4 # a и b - постоянные для вычисления размеров 0 и Х
b = cell - a
w = cell // 10 # толщина линий 0 и Х
w_l = (cell * 3) // cell * 3 # толщина линий сетки
eg_w = 300 # ширина доп. окна
eg_h = 200 # высота доп_окна
cl_f = "lightblue" # цвет поля
cl_0 = "red" # цвет ноликов
cl_X = "darkgreen" # цвет крестиков
cl_l = "gray" # цвет сетки игрового поля

win_pos = [[1,2,3], # матрица выигрышных позиций на поле
           [4,5,6],
           [7,8,9],
           [1,4,7],
           [2,5,8],
           [3,6,9],
           [1,5,9],
           [3,5,7],
           ]


def start_game():
    """
    Начальные координаты ходов человека и ИИ
    """
    return [[], []], [i for i in range(1,10)]


def create_field():
    """
    Отрисовка игрового поля и задание начальных координат
    """
    global xy, comp_turns
    xy, comp_turns = start_game() 
    canv.delete("all") # очистка игрового поля после завершения предыдущей игры
    canv.create_line(0, cell, cell*3, cell, width = w_l, fill = cl_l, dash = (w_l, w_l))
    canv.create_line(0, cell*2, cell*3, cell*2, width = w_l, fill = cl_l, dash = (w_l, w_l))
    canv.create_line(cell, 0, cell, cell*3, width = w_l, fill = cl_l, dash = (w_l, w_l))
    canv.create_line(cell*2, 0, cell*2, cell*3, width = w_l, fill = cl_l, dash = (w_l, w_l))
    canv.create_rectangle(0,0,cell*3, cell*3, width = w_l, outline = cl_l)
        
        
def draw_circle(event):
    """
    Отрисовка нолика
    """
    canv.create_oval(cell*(event.x // cell) + a, cell*(event.y // cell) + a, 
                     cell*(event.x // cell) + b, cell*(event.y // cell) + b, 
                     outline = cl_0, width = w)
  
    
def draw_cross(coord):
    """
    Отрисовка крестика
    """
    x = cell*((coord - 1) % 3)
    y = cell*((coord - 1) // 3)
    canv.create_line(x + a, y + a, 
                     x + b, y + b, 
                     fill = cl_X, width = w)
    canv.create_line(x + b, y + a, 
                     x + a, y + b, 
                     fill = cl_X, width = w)


# обработка хода игрока        
def turn_people(event, xy, comp_turns):
    """
    Обработка хода
    - ход игрока
    - если успешно, то ход компьютера
    """
    l.configure(text="Ваш ход")
    c = event.x // cell + (event.y // cell)*3 + 1 # расчет номера ячейки поля, куда кликнули мышкой (1-9)  
    if c in xy[0] or c in xy[1]: # если поле занято, то ...:
        l.configure(text="Поле занято!")        
    else: # а если свободно, то ...
        draw_circle(event) # ... рисуем нолик ...
        xy[0].append(c) # ... и добавляем номер ячейки в список ходов Игрока ...
        check_win(xy) # ... проверка на выигрыш Человека
        turn_comp(xy, comp_turns, c) # ... ход ИИ            


def choose_comp_coord(xy, comp_turns):
    """
    Логика ходов ИИ
    """
    #  проверка на возможность выигрышного хода для ИИ
    for index, item in enumerate(win_pos):
        coord = list(set(item) - set(xy[1])) # ... для ИИ
        if len(coord) == 1 and coord[0] in comp_turns: # ... если остался один ход и он возможен ...
            return coord[0]
    
    #  блокирование возможного выигрышного хода Человека    
    for index, item in enumerate(win_pos):
        coord = list(set(item) - set(xy[0])) # ... для Человека
        if len(coord) == 1 and coord[0] in comp_turns: # ... если остался один ход и он возможен ...          
            return coord[0]
        
    # пытаемся походить в угловые и центральную ячейку ...
    coord = list(set([1, 3, 7, 9, 5]) - set(xy[0]) - set(xy[1]))
    if coord:
        return r.choice(coord)
    
    # если ничего из вышестоящего не вышло, то комп ходит в бок ...
    return r.choice(list(set([2, 4, 6, 8]) - set(xy[0]) - set(xy[1])))
    
    
# обработка хода ИИ
def turn_comp(xy, comp_turns, c):
    """
    Обработка хода ИИ
    """
    comp_turns.remove(c) # удаляем из списка возможных ходов ИИ последний ход Человека
    if comp_turns: # если список ходов ИИ не пуст, то ...
        coord = choose_comp_coord(xy, comp_turns) # ... выбираем поле для хода ИИ ... 
        draw_cross(coord) # ... рисуем там крестик ...
        xy[1].append(coord) # добавляем это поле в список сделанных ходов ИИ ...
        comp_turns.remove(coord) # ... удаляем из списка возможных ходов ИИ это поле ..
    

def mouse_click(event, xy):
    """
    Обработка нажатия кнопки мыши
    """
    turn_people(event, xy, comp_turns)
    check_win(xy) # проверка на выигрыш после хода ИИ


def check_win(xy): 
    """
    Проверка результата хода
    """
    for index, item in enumerate(win_pos):
        if set(item) <= set(xy[0]):
            l.configure(text="Победил Человечище!")
            end_game()
        elif set(item) <= set(xy[1]):
            l.configure(text="Победила Железяка :(")
            end_game()
        elif not comp_turns:
            l.configure(text="Однако, ничья...")
            end_game()
            break

         
def end_game():
    """
    Всплывающее окно по окончании игры с запросом на продолжение
    """
    def next_game():
        create_field()
        eg.destroy()
        
    def exit_game():
        eg.destroy()
        root.destroy()
    
    eg = Toplevel(bg = "lightyellow")
    eg_x = root.winfo_rootx() + root.winfo_reqwidth() // 2
    eg_y = root.winfo_rooty() + root.winfo_reqheight() // 2 
    eg.geometry(f'300x100+{eg_x-eg_w//2}+{eg_y-eg_h//2}')
    eg.overrideredirect(True)
    Label(eg, text="Начать новую игру?", bg=eg['bg'], font=('Arial', 20)).pack(side=TOP, anchor="c", pady=5)
    Button(eg, text="Да", width=7, font=("",16), command=next_game).pack(side=LEFT, padx=10)
    Button(eg, text="Нет", width=7, font=("",16), command=exit_game).pack(side=RIGHT, padx=10)


# основное тело игры
if __name__ == "__main__":
    print(help(turn_people))
    root = Tk()
    root.title("Крестики-Нолики v 1.0")
    root_x = root.winfo_screenwidth() // 2 - cell*3//2
    root_y = root.winfo_screenheight() // 2 - cell*3//2
    root.resizable(width=False, height=False)
    root.geometry(f"+{root_x}+{root_y}") # центровка окна игры
    canv = Canvas(root, width=cell*3, height=cell*3, bg=cl_f, cursor="pencil")
    canv.pack()
    l = Label(text="Ходите первым!", font=("Arial", 24))
    l.pack()
    create_field()
    canv.bind('<1>', func=lambda event: mouse_click(event, xy))
    root.mainloop()