from model import (
    Mash, Effects, Appearance, Deck, Player
)

import random

_effects = [
    Effects(-2, (2, 'red'), 0),
    Effects(+1, -1, 0),
    Effects(-1, 0, -99),
    Effects(-1, -1, 1),
    Effects(0, -1, 0),
    Effects(-1, 0, 0),
    Effects(0, 0, 1),
    Effects(1, 0, -2),
    Effects(0, 0, (-1, 'red')),
    Effects(0, (-2, 'red'), 0),
    Effects(0, 1, (2, 'blue')),
    Effects(0, (1, 'blue'), 1),
    Effects(-2, 1, 2),
    Effects(0, -1, (-99, 'red')),
    Effects(1, 0, 1),
    Effects(0, (-1, 'red'), (-1, 'red')),
    Effects(-1, 0, 1),
    Effects(0, (-1, 'red'), 0),
    Effects(0, 1, 0),
    Effects(-1, 1, 1),
    Effects(0, 0, -1),
    Effects(-1, 0, -1),
    Effects(1, 1, 0),
    Effects(1, 0, 0),
    Effects(-1, -1, 0),
    Effects(-1, 1, 0),
    Effects(0, (1, 'red'), 0),
    Effects(1, 0, 1),
]

_cards = []

for i, c in enumerate(['red', 'blue', 'brown']):
    for j, s in enumerate(['a', 'b', 'c', 'd', 'e']):
        _cards.append(Appearance(c, s))

ci = iter(_cards)


def init_mashes():
    """
    色、形 と 効果をランダムに対応付ける
    色、形が 15 種類で少ないのでこっちをメインにループして効果を割り当てる
    :return:
    """
    cards = _cards[:]
    effects = _effects[:]

    random.shuffle(cards)
    random.shuffle(effects)

    result = []
    for ii, cc in enumerate(cards):
        result.append(Mash(cc, effects[ii]))

    return result


def init_deck(mashes):
    return Deck(mashes, 3)


def get_mash():
    return [
        next(ci),
        next(ci),
        next(ci),
        next(ci),
    ]


def init_players():
    n = 3
    return [Player(n), Player(n), Player(n), Player(n)]
