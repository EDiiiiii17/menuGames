import random

options = ["new game", "setting", "exit"]
selected_index = 0
player_name = ""

def print_menu():
    for i, option in enumerate(options):
        color_code = "\033[3{}m".format(i + 1)
        reset_code = "\033[0m"
        if i == selected_index:
            print(color_code + "->", option + reset_code)
        else:
            print("  ", option)

def start_game():
    if player_name == "":
        print("Пожалуйста, установите логин в пункте 'setting' перед началом игры.")
        return False

    print("Игра начинается! Игрок:", player_name)

    while True:
        board = []
        for _ in range(10):
            row = [' ' for _ in range(10)]
            board.append(row)

        player_row = 5
        player_col = 5
        board[player_row][player_col] = '@'

        level = 1
        num_enemies = level
        moves = 5
        total_moves = 0

        for _ in range(num_enemies):
            enemy_row = random.randint(0, 9)
            enemy_col = random.randint(0, 9)

            while (enemy_row == player_row and enemy_col == player_col) or board[enemy_row][enemy_col] == '+':
                enemy_row = random.randint(0, 9)
                enemy_col = random.randint(0, 9)

            board[enemy_row][enemy_col] = '+'

        while num_enemies > 0 and moves > 0:
            print(' *' * 11)

            for row in board:
                print('*', end=' ')
                for cell in row:
                    print(cell, end=' ')
                print('*')

            print(' *' * 11)

            direction = input("Введите направление (вверх - w, вниз - s, влево - a, вправо - d, выход - 0): ")

            if direction == '0':
                print("Выход из игры.")
                return Falses

            board[player_row][player_col] = ' '

            if direction == 'w' and player_row > 0:
                player_row -= 1
            elif direction == 's' and player_row < 9:
                player_row += 1
            elif direction == 'a' and player_col > 0:
                player_col -= 1
            elif direction == 'd' and player_col < 9:
                player_col += 1

            if board[player_row][player_col] == '+':
                board[player_row][player_col] = ' '
                num_enemies -= 1
                moves += 5

            if num_enemies == 0:
                level += 1
                num_enemies = level
                moves += 1

                for _ in range(num_enemies):
                    enemy_row = random.randint(0, 9)
                    enemy_col = random.randint(0, 9)

                    while (enemy_row == player_row and enemy_col == player_col) or board[enemy_row][enemy_col] == '+':
                        enemy_row = random.randint(0, 9)
                        enemy_col = random.randint(0, 9)

                    board[enemy_row][enemy_col] = '+'

            board[player_row][player_col] = '@'
            moves -= 1
            total_moves += 1

            print("Осталось ходов:", moves)

        if num_enemies == 0:
            print("Поздравляю, {}! Вы съели всех врагов!".format(player_name))
        else:
            print("У вас закончились ходы. Игра окончена!")
        print("Количество сделанных ходов:", total_moves)
        return True

def set_username():
    global player_name
    player_name = input("Введите ваш логин: ")
    print("Логин успешно установлен:", player_name)

def func_1():
    return start_game()

def func_2():
    set_username()

def func_3():
    print("Выход из игры.")
    return True

menu_d = {
    "new game": func_1,
    "setting": func_2,
    "exit": func_3
}

while True:
    print_menu()
    user_input = input()

    if user_input == "w":
        selected_index = (selected_index - 1) % len(options)
    elif user_input == "s":
        selected_index = (selected_index + 1) % len(options)
    elif user_input == "":
        selected_option = options[selected_index].lower()
        if selected_option in menu_d:
            func = menu_d[selected_option]
            game_over = func()
            if game_over:
                break
            else:
                continue
    elif user_input == "0":
        print("Выход из игры.")
        break
    else:
        print("Некорректный ввод. Попробуйте снова.")


