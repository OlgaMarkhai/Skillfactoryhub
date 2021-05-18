def greet():
    print("-------------------")
    print("  Добро пожаловать  ")
    print("      в игру       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" Как вводить значения: необходимо написать две цифры через пробел, где  ")
    print(" первое - номер строки  ")
    print(" второе - номер столбца ")
greet()
def cell():

    print("  0  1  2")
    for i in range(3):
     print(f"{i}{field[i][0]} {field[i][1]} {field[i][2]}")


def ask():
    while True:
        cords = input("Введите две цифры через пробел: ").split()

        if len(cords) != 2:
            print(" Вы должны вводить только 2 координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Вы должны вводить только числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y
def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!")
            return True
    return False

field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    cell()
    if count % 2 == 1:
        print(" Поставьте крестик")
    else:
        print(" Поставьте нолик")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = " X"
    else:
        field[x][y] = " 0"

    if check_win():
        break

    if count == 9:
        print(" Ничья!")
        break





