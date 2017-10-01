class Player:
    """
    プレイヤー
    """
    def __init__(self, n):
        """
        :param n: 効果が残るマッシュルームの数
        """
        self.hp = 3
        self.stomach = Stomach(n)

    def eat(self, mash):
        """
        食べる
        :param mash:
        :return:
        """
        self.stomach.mash[0] = mash

    def effect(self):
        """
        効果が発生する
        :return:
        """
        for i, m in enumerate(self.stomach.mash):
            if m is not None:
                e = m.effects.effect[i]
                if isinstance(e, tuple):
                    self.hp += e[0]
                else:
                    self.hp += e

    def is_dead(self):
        """
         死んだかどうか
         """
        return self.hp <= 0

    def __str__(self):
        return 'p[' + str(self.hp) + ',' + str(self.stomach) + ']'


class Stomach:
    """
    胃袋
    指定数分のマッシュルームがたまる
    """
    def __init__(self, n):
        self.n = n
        # バッファとして一個余分に持つ
        self.mash = [None] * (n + 1)

    def digest(self):
        self.mash = [None] + self.mash[:self.n - 1]

    def __str__(self):
        result = 'st['
        for m in self.mash:
            result += str(m) + ','
        result += ']'
        return result


class Effects:
    """
    効果
    ３日分の効果をもつ
    """
    def __init__(self, effect1, effect2, effect3):
        self.effect = []
        self.effect.append(effect1)
        self.effect.append(effect2)
        self.effect.append(effect3)

    def __str__(self):
        return 'e[' + str(self.effect) + ']'


class Appearance:
    """
    見た目
    形と色のタプル
    """
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    def __str__(self):
        return 'app[' + str(self.shape) + ',' + str(self.color) + ']'


class Mash:
    """
    マッシュルーム
    見た目と効果のタプル
    """
    def __init__(self, appearance, effects):
        self.appearance = appearance
        self.effects = effects

    def __str__(self):
        return 'm[' + str(self.appearance) + ',' + str(self.effects) + ']'


class Deck:
    """
    山札
    見た目をそれぞれ指定数分増やして持たせる
    """
    def __init__(self, mashes, n):
        d = []
        for m in mashes:
            for i in range(n):
                d.append(m)

        self.d = d
        self.iter = iter(d)

    def next(self):
        return next(self.iter)

    def gather(self, number):
        r = []
        for i in range(number):
            r.append(self.next())

        return r

    def __str__(self):
        return 'deck[' + str([str(x) for x in self.d]) + ']'
