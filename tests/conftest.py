import pytest


@pytest.fixture
def list_without_win_combo():
    return [str(n + 1) for n in range(9)]


@pytest.fixture
def list_with_win_combo():
    return ['x' for n in range(9)]


@pytest.fixture
def field(list_without_win_combo):
    return '\n - - -' \
        '\n|{}|{}|{}|'\
        '\n - - -' \
        '\n|{}|{}|{}|' \
        '\n - - -' \
        '\n|{}|{}|{}|' \
        '\n - - -\n'.format(
            list_without_win_combo[0], list_without_win_combo[1], list_without_win_combo[2],
            list_without_win_combo[3], list_without_win_combo[4], list_without_win_combo[5],
            list_without_win_combo[6], list_without_win_combo[7], list_without_win_combo[8],
        )
