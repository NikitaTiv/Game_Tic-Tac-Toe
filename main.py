from random import shuffle, choice
from enums import TicTacToeSymbol, TicTacToePlayer


def field(list_cells: list[str]) -> str:
    """Строит поле."""
    field = '\n - - -' \
            '\n|{}|{}|{}|'\
            '\n - - -' \
            '\n|{}|{}|{}|' \
            '\n - - -' \
            '\n|{}|{}|{}|' \
            '\n - - -\n'.format(
                list_cells[0], list_cells[1], list_cells[2],
                list_cells[3], list_cells[4], list_cells[5],
                list_cells[6], list_cells[7], list_cells[8],
            )
    return field


def choose_user_symbol(symbols: TicTacToeSymbol) -> tuple[str, str]:
    """Выбирает кем будет играть игрок и компьтер."""
    player_symbols = list(symbols)
    shuffle(player_symbols)
    return player_symbols[0].value, player_symbols[1].value


def result_of_move_bool(list_cells: list[str]) -> bool:
    """Проверяет победил ли участник."""
    win_coord = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6),
    )
    for row in win_coord:
        if list_cells[row[0]] == list_cells[row[1]] == list_cells[row[2]]:
            return True
    return False


def ask_user_move(list_cells: list[str]) -> str:
    """Просит у пользователя сделать ход и проверяет его."""
    while True:
        player_move = input('Ваш ход: ')
        variants_of_moves = [cell for cell in list_cells if cell.isdigit()]
        if player_move in variants_of_moves:
            break
        else:
            print('Введите корректную ячейку.')
            continue
    return player_move


def make_pc_move(list_cells: list[str]) -> str:
    """Делает ход за ПК."""
    variants_of_moves = [cell for cell in list_cells if cell.isdigit()]
    pc_move = choice(variants_of_moves)
    print(f'Ход компьютера {pc_move}')
    return pc_move


if __name__ == '__main__':
    list_cells = [str(n + 1) for n in range(9)]
    user_symbol, pc_symbol = choose_user_symbol(TicTacToeSymbol)
    print(f'Вы играете за {user_symbol}, компьтер за {pc_symbol}')
    counter = 0
    while True:
        print(field(list_cells))
        player = TicTacToePlayer.User if counter % 2 == 0 else TicTacToePlayer.Compukter
        player_symbol = user_symbol if counter % 2 == 0 else pc_symbol
        if player == TicTacToePlayer.User:
            player_move = ask_user_move(list_cells)
        if player == TicTacToePlayer.Compukter:
            player_move = make_pc_move(list_cells)
        list_cells[int(player_move) - 1] = player_symbol
        result_game = result_of_move_bool(list_cells)
        if result_game:
            print(f'Победил {player.value}')
            break
        list_free_cells = [_ for _ in list_cells if _.isdigit()]
        if not list_free_cells:
            print('Ничья')
            break
        counter += 1
