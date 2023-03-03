import enum


class TicTacToeSymbol(enum.Enum):
    """Символы для игры в крестики-нолики."""

    x = 'x'
    o = 'o'


class TicTacToePlayer(enum.Enum):
    """Имена игроков."""

    User = 'User'
    Compukter = 'Compukter'
