from random import choice
from typing import Union


def field(list_user_choice: list[Union[int, str]]) -> str:
    """Строит поле."""
    field = '\n - - -' \
            '\n|{}|{}|{}|'\
            '\n - - -' \
            '\n|{}|{}|{}|' \
            '\n - - -' \
            '\n|{}|{}|{}|' \
            '\n - - -\n'.format(
                list_user_choice[0], list_user_choice[1], list_user_choice[2],
                list_user_choice[3], list_user_choice[4], list_user_choice[5],
                list_user_choice[6], list_user_choice[7], list_user_choice[8],
            )

    return field


def choose_user_sign() -> str:
    """Выбирает кем будет играть игрок."""
    player_sign = choice(['x', 'o'])
    print(f'\n\nВы будете играть за {player_sign}')

    return player_sign


def record_players_move(
    type_sign: str, move: str, list_user_choice: list[Union[int, str]], list_cell: list[int],
) -> list[int | str]:
    """Записывает ходы игроков."""
    list_user_choice[int(move)-1] = type_sign
    del list_cell[int(move)]

    return list_user_choice


def result_of_move_bool(list_user_choice: list[Union[int, str]]) -> bool:
    """Проверяет победил ли участник."""
    win_coord = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6),
    )
    for row in win_coord:
        if list_user_choice[row[0]] == list_user_choice[row[1]] == list_user_choice[row[2]] != ' ':
            return True
    return False


def announcement(result: str) -> str:
    """Обявляет результат."""
    if result == 'draw':
        return 'Ничья'
    return f'В этой партии победил {result}'


def result_game(winner_or_draw: str, list_user_choice: list[Union[int, str]]) -> bool:
    """Подводит итоги игры и предалагает сыгать еще."""
    print(field(list_user_choice))
    print(announcement(winner_or_draw))
    question = input('Хотите сыграть еще? (Да/Нет) ')
    if question.lower() == 'да':
        return True
    elif question.lower() == 'нет':
        return False


def choose_pc_sign(player_sign: str) -> str:
    """Назначает символ компьютеру."""
    if player_sign == 'x':
        return 'o'
    if player_sign == 'o':
        return 'x'


def choose_move(player: str, list_cell: list[Union[int, str]]) -> int:
    """Просит пользователя сделать ход и делает ход за ПК."""
    while True:
        if player == 'игрок':
            player_move = int(input('Ваш ход: '))
            if player_move not in list_cell:
                print('Введите корректную ячейку.')
                continue
        if player == 'компьютер':
            player_move = choice(list_cell)
            print(f'Ход компьютера {player_move}')
        break
    return player_move


if __name__ == '__main__':
    active = True
    while active:
        list_user_choice = [n+1 for n in range(9)]  # список для отрисовки таблицы
        list_cell = [n+1 for n in range(9)]  # из этого удаляются значения, выбора ходов пк
        counter = 0
        player_sign = choose_user_sign()
        while True:
            print(list_user_choice)
            player = 'игрок'
            if len(list_cell) % 2 == 0:
                player = 'компьютер'
            if len(list_cell) < 9:
                player_sign = choose_pc_sign(player_sign)
            print(field(list_user_choice))
            move_crosses = choose_move(player, list_cell)
            list_user_choice = record_players_move(
                player_sign, move_crosses, list_user_choice, list_cell,
            )
            counter += 1
            result = result_of_move_bool(list_user_choice)
            if result:
                continue_game = result_game(player, list_user_choice)
                if continue_game:
                    break
                else:
                    active = False
                    break
            if counter == 9:
                continue_game = result_game('draw', list_user_choice)
                if continue_game:
                    break
                else:
                    active = False
                    break
