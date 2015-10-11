# class Card(object):
#     symbols = []
#
#     def get_connected_cards(self):
#         connected_cards = []
#         for symbol in self.symbols:
#             if symbol in cards:
#                 connected_cards.push()
#
#
# class Generator(object):
#     cards = []
#     last_symbol = 0
#     symbols = {}
#     connections = {}
#
#     def add_new_symbol(self):
#         self.last_symbol += 1
#         self.symbols[self.last_symbol] = []
#
#     def generate(self):
#         card = ()
import math

possible_symbols = [
    'ant',
    'bat',
    'cat',
    'dog',
    'eel',
    'fox',
    'gorilla',
    'hare',
]

card_num = 5
connections = []
card_pairs = []
symbols = {
    'ant': [],
    'bat': [],
    'cat': [],
    'dog': [],
    'eel': [],
    'fox': [],
    'gorilla': [],
    'hare': [],
}
cards = {}

def get_symbol(c1, c2):
    for p in possible_symbols:
        if not (c1 in symbols[p] and c2 in symbols[p]):
            return p

for c1 in range(card_num):
    for c2 in range(card_num):
        if not c1 == c2 and (c1, c2) not in card_pairs and (c2, c1) not in card_pairs:
            symbol = get_symbol(c1, c2)
            connections.append((c1, symbol, c2))
            symbols[symbol] += [c1, c2]
            card_pairs.append((c1, c2))
            try:
                cards[c1].append(symbol)
            except KeyError:
                cards[c1] = [symbol]
            try:
                cards[c2].append(symbol)
            except KeyError:
                cards[c2] = [symbol]


for c, s in cards.items():
    print("%d: %s" % (c, ', '.join(set(s))))