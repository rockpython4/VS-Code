# Создаем бесконечный цикл для поддержки игры. Выходить будем через break
print("Игра Крестики-Нолики для двух игроков")
# Создаем поле
field = [
    [' ', '1', '2', '3'],
    ['1', '-', '-', '-'],
    ['2', '-', '-', '-'],
    ['3', '-', '-', '-']
]

#field = [
#    [' ', '1', '2', '3'],
#    ['1', '0', '0', 'X'],
#    ['2', '0', 'X', '0'],
#    ['3', 'X', '0', '0']
#]

# Чья очередь? 0 - Первый игрок (X), 1 - Второй игрок (0)
whos_turn = 0
# Флаг окончания игры
game_over = False


# функция печатает текущее поле
def print_field():
    for each_st in field:
        print(" ".join(each_st), sep = ' ')
 
# функция проверяет есть ли победа игрока 1 (player_num = 0) или 2 (player_num = 1)
def check_field_win(player_num) -> bool:
    sign = 'X' if player_num == 0 else 'Y'
     # сначала проверяем строки
    for each_st in field:
        if "".join(each_st[1:4]) == sign * 3:
            return True
    # потом проверяем столбцы
    for i in range(1, len(field)):
        if "".join(list(map(lambda x: x[i], field[1:4]))) == sign * 3:
            return True
    # проверяем диагонали
    if "".join([field[1][1], field[2][2], field[3][3]]) == sign * 3 or "".join([field[1][3], field[2][2], field[3][1]]) == sign * 3:
        return True
 
# функция проверяет, заполнено ли все поле крестиками и ноликами (для определения ничьей)
def check_full() -> bool:
    for each_st in field:
        for each_cl in each_st:
            if each_cl == '-':
                return False
    return True
 
    
while not game_over:
    print('----------------------------------------------------')
    print(f"Ход игрока {whos_turn + 1}")
    print("Текущее поле боя:")
    print_field()
    while True:
        i, j = map(int, str(input("Ввведите через пробел номер строки и номер столбца: ")).split(' '))
        if field[i][j] in ('X', '0'):
            print('----------------------------------------------------')
            print("Эта клетка уже занята, введите другое поле для атаки")
            break
        field[i][j] = 'X' if whos_turn == 0 else '0'
        if check_field_win(whos_turn):
            print('----------------------------------------------------')
            print(f"Игрок {whos_turn + 1} победил!")
            print_field()
            game_over = True
            break
        if check_full():
            print('----------------------------------------------------')
            print('Игра закончилась вничью!')
            print_field()
            game_over = True
            break
        whos_turn = 1 - whos_turn
        break
        