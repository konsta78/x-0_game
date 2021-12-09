from tkinter import *

"""
field:

1 2 3
4 5 6
7 8 9
"""
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

#отрисовка игрового поля
def redraw_field():
    global xy
    global turn
    global flag_game
    turn = 0 # ход Игрока 1 (Игрок 2 - turn = 1)
    xy = [[], []] # координаты ходов игроков
    flag_game = True # флаг активности игры
    canv.delete("all") # очистка игрового поля после завершения предыдущей игры
    # отрисовка сетки игрового поля:
    canv.create_line(0, cell, cell*3, cell, width = w_l, fill = cl_l, dash = (w_l, w_l))
    canv.create_line(0, cell*2, cell*3, cell*2, width = w_l, fill = cl_l, dash = (w_l, w_l))
    canv.create_line(cell, 0, cell, cell*3, width = w_l, fill = cl_l, dash = (w_l, w_l))
    canv.create_line(cell*2, 0, cell*2, cell*3, width = w_l, fill = cl_l, dash = (w_l, w_l))
    canv.create_rectangle(0,0,cell*3, cell*3, width = w_l, outline = cl_l)
    
    l.configure(text="Ход игрока 1")

# проверка наличия на поле выигрышных комбинаций
# и останов игры в случае наличия таковых
def win(win_pos, xy, turn):
    global flag_game
    if 2 < len(xy[0]) <= 5: # проверка на выигрыш начинается только после третьего хода 'X' и до 5-го
        for i, j in enumerate(win_pos):
            if j[0] in xy[(turn+1)%2] and j[1] in xy[(turn+1)%2] and j[2] in xy[(turn+1)%2]:
                l.configure(text=f"Игрок {(turn+1)%2+1} Выиграл! Победа!")
                flag_game = False
                break
    if len(xy[0] + xy[1]) == 9:
        l.configure(text="Ничья! Победила дружба :)")
        flag_game = False
    if not flag_game:
        end_game()
        
# отрисока нолика
def draw_circle(event):
    canv.create_oval(cell*(event.x // cell) + a, cell*(event.y // cell) + a, 
                     cell*(event.x // cell) + b, cell*(event.y // cell) + b, 
                     outline = cl_0, width = w)
    
# отрисовка крестика
def draw_cross(event):
    canv.create_line(cell*(event.x // cell) + a, cell*(event.y // cell) + a, 
                     cell*(event.x // cell) + b, cell*(event.y // cell) + b, 
                     fill = cl_X, width = w)
    canv.create_line(cell*(event.x // cell) + b, cell*(event.y // cell) + a, 
                     cell*(event.x // cell) + a, cell*(event.y // cell) + b, 
                     fill = cl_X, width = w)

# обработка хода игрока        
def draw_sym(event): 
    global xy
    global turn
    c = event.x // cell + (event.y // cell)*3 + 1 # расчет номера ячейки поля, куда кликнули мышкой (1-9)
        
    if c not in xy[0] and c not in xy[1] and turn == 0: # если ячейка пуста и ход Игрока 1, то:
        draw_circle(event) # ... рисуем нолик ...
        xy[turn].append(c) # ... и добавляем номер ячейки в список ходов Игрока 1 ...
        turn = 1 # ... и передаем ход Игроку 2
        
    elif c not in xy[1] and c not in xy[0] and turn == 1: # если ячейка пуста и ход Игрока 2, то:
        draw_cross(event) # ... рисуем крестик ...
        xy[turn].append(c) # ... и добавляем номер ячейки в список ходов Игрока 2 ...
        turn = 0 # ... и передаем ход Игроку 1
    l.configure(text=f"Ход игрока: {turn+1}")
    win(win_pos, xy, turn)

# обработка нажатия левой кнопки мыши
def mouse_click(event): 
    global flag_game
    if flag_game:
        draw_sym(event)
                
def end_game():
    def next_game():
        redraw_field()
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
    Button(eg, text="Да", width=7, font=("",16), command = next_game).pack(side=LEFT, padx=10)
    Button(eg, text="Нет", width=7, font=("",16), command = exit_game).pack(side=RIGHT, padx=10)


# тело игры
root = Tk()
root.title("Крестики-Нолики v 1.0")
root_x = root.winfo_screenwidth() // 2 - cell*3//2
root_y = root.winfo_screenheight() // 2 - cell*3//2
root.resizable(width = False, height = False)
root.geometry(f"+{root_x}+{root_y}") # центровка окна игры

canv = Canvas(root, width = cell*3, height = cell*3, bg = cl_f, cursor="pencil")
canv.pack()
l = Label(text="Ход игрока 1", font = ("Arial", 24))
l.pack() 
redraw_field()
canv.bind('<1>', mouse_click)
root.mainloop()
