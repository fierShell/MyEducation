def new_field():
    new_field = ['-', '-', '-',
                 '-', '-', '-',
                 '-', '-', '-']
    return new_field


# Отрисовка поля
def print_field(field):
    print(field[0], field[1], field[2], sep='|')
    print(field[3], field[4], field[5], sep='|')
    print(field[6], field[7], field[8], sep='|')


def rules():
    print("Для установки крестика или нолика в ячейку укажите позцицю:")
    print('1', '2', '3', sep='|')
    print('4', '5', '6', sep='|')
    print('7', '8', '9', sep='|', end="\n\n")


# проверка победы
def win_check(symbol, field):
    # Победные комбинации
    win_condition = [[0, 1, 2],
                     [3, 4, 5],
                     [6, 7, 8],
                     [0, 3, 6],
                     [1, 4, 7],
                     [2, 5, 8],
                     [2, 4, 6],
                     [0, 4, 8]]

    for check in win_condition:
        if field[check[0]] == field[check[1]] == field[check[2]] == 'x' or field[check[0]] == field[check[1]] == field[
            check[2]] == 'y':
            print(f'Победил {symbol} ')
            return 1


# Проверям правильность ввода
def check_value(field):
    move = input("Введите позицию: ")
    check = False
    while check == False:

        try:
            int_move = int(move)
            if 0 < int_move <= 9:
                return int_move
            else:
                print("Введите значение от 0 до 9", end="\n\n")
                move = input()

        except ValueError:
            print("Могут быть только значения от 0 до 9", end="\n\n")
            move = input()

        # Проверка занята ли ячейка, и установка значения в ячейку


def place_position(symbol, field):
    move = check_value(field)
    check = False
    while check == False:

        if field[move - 1] == "x" or field[move - 1] == "o":
            print("Данная ячейка уже занята", end='\n')
            move = check_value(field)
        else:
            field[move - 1] = symbol
            check = True


# Игра
def game(field):
    count = 0
    # поочередная смена o и x
    win = False
    while win == False:
        if count % 2 == 0:
            symbol = 'x'
        else:
            symbol = 'o'
        print(f"Ход игрока {symbol}:")
        place_position(symbol, field)

        print("", end='\n')
        print_field(field)
        print("", end='\n')

        if count > 3:
            if win_check(symbol, field) == 1:
                print("-" * 16)
                win = True
                return symbol
        if count == 8:
            win = True
            print("ничья")
            print("-" * 16)

        count += 1


# Раунды игр
def main():
    rules()
    ask = "да"
    field = new_field()

    # сообщение о смене игроков
    number_of_round = 0
    if number_of_round % 2 == 0:
        print("Первым ходит 1 игрок")
    else:
        print("Первым ходит 2 игрок")

        # повторный запуск игры по запросу
    while ask == 'Да' or ask == 'да':
        field = new_field()
        print(f"Номер раунда {number_of_round + 1}", end="\n\n")

        game(field) == symbol

        number_of_round += 1
        field = new_field()

        print("Введите Да для продолжения", end="\n\n")
        answer = input()


main()