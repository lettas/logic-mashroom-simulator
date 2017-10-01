import sys
from logging import basicConfig, getLogger, INFO, DEBUG

import input

basicConfig(level=INFO)
logger = getLogger(__name__)


def eat(players, mashes):
    """
    食べる
    :param players:
    :param mashes:
    :return:
    """
    for p in zip(players, mashes):
        p[0].eat(p[1])


def effect(players):
    """
    効果が発生する
    :param players:
    :return:
    """
    for p in players:
        p.effect()


def is_dead(players):
    """
    誰か死んだかどうか
    :param players:
    :return:
    """
    for p in players:
        if p.is_dead():
            return True
    return False


def digest(players):
    """
    消化する
    :param players:
    :return:
    """
    for p in players:
        p.stomach.digest()


def log_state(iter_num, players):
    """
    状態をログ出力
    :param iter_num:
    :param players:
    :return:
    """
    for p in players:
        logger.debug('%s, %s', iter_num, p)


if __name__ == '__main__':

    mashes = input.init_mashes()
    deck = input.init_deck(mashes)

    #logger.debug(str([str(x) for x in mashes]))
    #logger.debug(deck)
    players = input.init_players()

    #log_state(0, players)
    for d in range(1, 7):
        g_maches = deck.gather(len(players))
        eat(players, g_maches)
        effect(players)
        if is_dead(players):
            log_state(d, players)
            print("Dead " + str(d))
            sys.exit()
        #log_state(d, players)
        digest(players)

    log_state(7, players)
    print("Survived")
