from enums import TicTacToeSymbol
from main import choose_user_symbol, result_of_move_bool, build_field, make_pc_move


def test__field__correctly_build_field(list_without_win_combo, field):
    assert build_field(list_without_win_combo) == field


def test__choose_user_symbol__return_correct_meaning():
    assert len(choose_user_symbol(list(TicTacToeSymbol))) == 2
    assert choose_user_symbol(list(TicTacToeSymbol)).count('x') == 1
    assert choose_user_symbol(list(TicTacToeSymbol)).count('o') == 1


def test__result_of_move_bool__check_list_with_win_combination(list_with_win_combo):
    assert result_of_move_bool(list_with_win_combo)


def test__result_of_move_bool__check_list_without_win_combination(list_without_win_combo):
    assert not result_of_move_bool(list_without_win_combo)


def test__make_pc_move__check_correctness_return(list_without_win_combo):
    assert make_pc_move(list_without_win_combo) in list_without_win_combo
    assert len(make_pc_move(list_without_win_combo)) == 1
