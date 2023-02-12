from random import choice


def field(dict_user_choice: dict) -> str:
    """Строит поле."""
    empty_dict = {
        'A1': ' ', 'B1': ' ', 'C1': ' ', 'A2': ' ',
        'B2': ' ', 'C2': ' ', 'A3': ' ', 'B3': ' ', 'C3': ' ',
    }

    for cell, meaning in dict_user_choice.items():
        if cell in empty_dict:
            empty_dict[cell] = meaning

    field = '\n   A B C' \
            '\n   - - -' \
            '\n1 |{}|{}|{}|'\
            '\n   - - -' \
            '\n2 |{}|{}|{}|' \
            '\n   - - -' \
            '\n3 |{}|{}|{}|' \
            '\n   - - -\n'.format(
                empty_dict['A1'], empty_dict['B1'], empty_dict['C1'],
                empty_dict['A2'], empty_dict['B2'], empty_dict['C2'],
                empty_dict['A3'], empty_dict['B3'], empty_dict['C3'],
            )

    return field


def record_players_move(
    type_player: str, move: str, dict_user_choice: dict, list_cell: list,
) -> dict | None:
    """Записывает ходы игроков."""
    if type_player == 'user':
        dict_user_choice[move] = 'x'
    if type_player == 'pc':
        dict_user_choice[move] = 'o'
    list_cell.remove(move)

    return dict_user_choice


def make_pc_move(list_cell: list) -> str:
    """Делает ход компьютера."""
    return choice(list_cell)


def result_of_move(dict_user_choice: dict, player_element: str) -> str:
    """Проверяет победил ли участник."""
    list_user_move = [
        move for move, meaning in dict_user_choice.items() if meaning == player_element
    ]
    if 'A1' in list_user_move and 'B2' in list_user_move and 'C3' in list_user_move:
        return 'win'
    if 'A3' in list_user_move and 'B2' in list_user_move and 'C1' in list_user_move:
        return 'win'
    if 'A1' in list_user_move and 'B1' in list_user_move and 'C1' in list_user_move:
        return 'win'
    if 'A2' in list_user_move and 'B2' in list_user_move and 'C2' in list_user_move:
        return 'win'
    if 'A3' in list_user_move and 'B3' in list_user_move and 'C3' in list_user_move:
        return 'win'
    if 'A1' in list_user_move and 'A2' in list_user_move and 'A3' in list_user_move:
        return 'win'
    if 'B1' in list_user_move and 'B2' in list_user_move and 'B3' in list_user_move:
        return 'win'
    if 'C1' in list_user_move and 'C2' in list_user_move and 'C3' in list_user_move:
        return 'win'


def announcement(result: str) -> str:
    """Обявляет результат."""
    if result == 'draw':
        return 'Ничья'
    return f'В этой партии победил {result}'


if __name__ == '__main__':
    active = True
    while active:
        dict_user_choice = {}
        list_cell = [
            'A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3',
        ]
        for _ in range(8):
            print(field(dict_user_choice))
            user_move = input('Ваш ход: ')
            if user_move not in list_cell:
                print('Введите корректное значение.')
                continue
            dict_user_choice = record_players_move(
                'user', user_move, dict_user_choice, list_cell,
            )
            result_user = result_of_move(dict_user_choice, 'x')
            if result_user == 'win':
                print(field(dict_user_choice))
                print(announcement('игрок'))
                question = input('Хотите сыграть еще? (Да/Нет) ')
                if question.lower() == 'да':
                    break
                elif question.lower() == 'нет':
                    active = False
                    break
            try:
                pc_move = make_pc_move(list_cell)
            except IndexError:
                print(field(dict_user_choice))
                print(announcement('draw'))
                question = input('Хотите сыграть еще? (Да/Нет) ')
                if question.lower() == 'да':
                    break
                elif question.lower() == 'нет':
                    active = False
                    break
            print(f'- - - - -\nХод компьютера {pc_move}.')
            dict_user_choice = record_players_move(
                'pc', pc_move, dict_user_choice, list_cell,
            )
            result_pc = result_of_move(dict_user_choice, 'o')
            if result_pc == 'win':
                print(field(dict_user_choice))
                print(announcement('компьютер'))
                question = input('Хотите сыграть еще? (Да/Нет) ')
                if question.lower() == 'да':
                    break
                elif question.lower() == 'нет':
                    active = False
                    break
